from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Playlist(db.Model):
    playlist_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(100))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    public = db.Column(db.Boolean, nullable=False)
    likes = db.Column(db.Integer,default=0)
    shares = db.Column(db.Integer,default=0)
    plays = db.Column(db.Integer,default=0)
    song_id = db.Column(db.Integer, db.ForeignKey('songs.song_id'), nullable=False)
    song = db.relationship('Song', backref=db.backref('songs', lazy=True))

    def create_playlist():
        pass

    def update_playlist():
        pass

    def delete_playlist():
        pass

    def get_playlist():
        pass

    def get_top_playlist():
        #get 50 of the most popular public playlists(load 50 more once they reach the bottom of the container) - explore
        pass

    def toggle_playlist_share():
        #toggles if the playlist is public or private
        pass
