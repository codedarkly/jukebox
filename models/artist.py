from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Artist(db.Model):
    artist_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def add_artist():
        pass
