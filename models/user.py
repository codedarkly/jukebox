from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from email_validator import validate_email, EmailNotValidError
from datetime import datetime
import smtplib
from email.message import EmailMessage
import re
import random
import string
import time

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(50),nullable=False)
    username = db.Column(db.String(50),unique=True, nullable=False)
    email = db.Column(db.String(50),unique=True,nullable=False)
    image = db.Column(db.String(100),default='/static/images/default-user.png')
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    last_active = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    status = db.Column(db.String(8),default='active')

    @validates('fullname')
    def validate_fullname(self, key, fullname):
        pattern = r'^[A-Za-z]+(?:\'[A-Za-z]+)?(?:-[A-Za-z]+)?(?:\s[A-Za-z]+(?:\'[A-Za-z]+)?(?:-[A-Za-z]+)?)*$'
        if len(fullname) > 50:
            raise ValueError('Full name cannot be more than 50 characters')
        elif not re.match(pattern, fullname):
            raise ValueError('Name must consist of only letters')
        return fullname

    @validates('username')
    def validate_username(self, key, username):
        if len(username) > 50:
            raise ValueError('Username must be less than 50 characters')
        elif not re.match("^[a-zA-Z0-9_]+$", username):
            raise ValueError('Username can only be letters,numbers and underscores')
        return username

    def validate_email_field(self, email):
        try:
            user_email = validate_email(email, check_deliverability=True)
            normalized_email = user_email.normalized
            return normalized_email
        except EmailNotValidError as e:
            return str(e)

    @staticmethod
    def generate_passcode():
        #generate a passcode of 8 characters and store it in redis(expire it in 10 minutes)
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))

    @staticmethod
    def mail_passcode(**data):
       #send email with generated passcode
       msg = EmailMessage()
       msg['to'] = data['email']
       msg['subject'] = data['subject']
       msg['from'] = data['sender']
       msg.set_content(data['template'], subtype='html')
       with smtplib.SMTP_SSL(data['server'], data['port']) as smtp:
           smtp.login(data['username'] , data['password'])
           smtp.send_message(msg)
       return 200

    @staticmethod
    def cache_passcode(rc, user):
        user_registration = f'username:{user["username"]}'
        rc.hset(user_registration, mapping=user)
        rc.expire(user_registration, 900)
        rc_result = rc.hgetall(user_registration)
        data = {k.decode():v.decode() for k,v in rc_result.items()}
        return data

    @staticmethod
    def verify_passcode(rc, **user):
        #verify that the passcode matches account
        try:
            rc_result = rc.hgetall(user['username'])
            data = {k.decode():v.decode() for k, v in rc_result.items()}
            return data['passcode']
        except KeyError:
            return 'Your passcode or username is incorrect or your passcode has expired', 401

    def signin(self, email):
        pass

    @staticmethod
    def register_account(user):
        if user is not None:
            db.session.add(user)
            db.session.commit()
        return 'User added', 200

    @staticmethod
    def check_for_account_existence(user):
        #check database for user account
        result = User.query.filter_by(email=user.email).first()
        if result:
            return 'User exists', 409
        else:
            return User.register_account(user)


    def signout():
        pass

    def deactivate_account():
        pass

    def update_account():
        pass

    def get_account():
        pass
