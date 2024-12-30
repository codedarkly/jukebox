from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Album(db.Model):
    album_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(75),nullable=False)
    cover = db.Column(db.String(100))
    duration = db.Column(db.Integer)
    release_date = db.Column(db.DateTime)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.artist_id'), nullable=False)
    artist = db.relationship('Artist', backref=db.backref('artists', lazy=True))
