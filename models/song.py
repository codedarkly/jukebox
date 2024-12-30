from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Song(db.Model):
    song_id = db.Column(db.Integer, primary_key=True)
    song_title = db.Column(db.String(100),nullable=False)
    duration = db.Column(db.Integer)
    release_date = db.Column(db.DateTime)
    plays = db.Column(db.Integer,default=0)
    likes = db.Column(db.Integer,default=0)
    shares = db.Column(db.Integer, default=0)
    public = db.Column(db.Boolean, nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.artist_id'),nullable=False)
    album_id = db.Column(db.Integer, db.ForeignKey('albums.album_id'),nullable=False)
    jukebox_id = db.Column(db.Integer, db.ForeignKey('jukebox.jukebox_id'),nullable=False)
    artist = db.relationship('Artist', backref=db.backref('artists', lazy=True))
    album = db.relationship('Album', backref=db.backref('albums', lazy=True))
    jukebox = db.relationship('Jukebox', backref=db.backref('jukebox', lazy=True))

    def add_song():
        pass

    def update_song_title():
        pass

    def remove_song():
        pass

    def get_song():
        pass

    def get_popular_songs():
        #top 50 most public popular songs - explore
        pass

    def toggle_song_share():
        pass

    def song_of_the_day():
        #get the most popular song of the day
        pass
