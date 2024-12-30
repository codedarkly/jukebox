from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100),nullable=False)
    username = db.Column(db.String(75),unique=True, nullable=False)
    email = db.Column(db.String(75),unique=True,nullable=False)
    image = db.Column(db.String(100))
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    last_active = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


    def registration():
        pass

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
