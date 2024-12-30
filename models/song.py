from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Song(db.Model):
    song_id = db.Column(db.Integer, primary_key=True)
    song_title = db.Column(db.String(100),nullable=False)
    duration = db.Column(db.Integer)
    release_date = db.Column(db.DateTime)
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.artist_id'),nullable=False)
    album_id = db.Column(db.Integer, db.ForeignKey('albums.album_id'),nullable=False)
    jukebox_id = db.Column(db.Integer, db.ForeignKey('jukebox.jukebox_id'),nullable=False)
    artist = db.relationship('Artist', backref=db.backref('artists', lazy=True))
    album = db.relationship('Album', backref=db.backref('albums', lazy=True))
    jukebox = db.relationship('Jukebox', backref=db.backref('jukebox', lazy=True))
