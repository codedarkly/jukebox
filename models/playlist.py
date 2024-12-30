from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Playlist(db.Model):
    playlist_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(100))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    song_id = db.Column(db.Integer, db.ForeignKey('songs.song_id'), nullable=False)
    song = db.relationship('Song', backref=db.backref('songs', lazy=True))
