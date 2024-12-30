from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from email_validator import validate_email, EmailNotValidError
from datetime import datetime
import re

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(50),nullable=False)
    username = db.Column(db.String(50),unique=True, nullable=False)
    email = db.Column(db.String(50),unique=True,nullable=False)
    image = db.Column(db.String(100),default='/static/images/default-user.png')
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    last_active = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    @validates('fullname')
    def validate_fullname(self, key, fullname):
        if len(fullname) > 50:
            raise ValueError('Full name cannot be more than 50 characters')
        elif not re.match("^[a-zA-Z]+$", fullname):
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







    def signin():
        pass

    def signout():
        pass

    def check_accounts():
        #check for user account
        pass

    def verify_passcode():
        #verify that the passcode matches account
        pass

    def deactivate_account():
        pass

    def generate_passcode():
        #generate a passcode of 8 characters and store it in redis(expire it in 10 minutes)
        pass

    def update_account():
        pass

    def get_account():
        pass

    def mail_passcode():
        #send email with generated passcode
        pass
