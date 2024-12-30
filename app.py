from flask import Flask, render_template, url_for, redirect
from models.user import db, User
from models.artist import Artist
from models.album import Album
from models.genre import Genre
from models.jukebox import Jukebox
from models.playlist import Playlist
from models.song import Song
from dotenv import load_dotenv
from datetime import datetime
import os

load_dotenv('.env')

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
db.init_app(app)


@app.route('/', methods=['GET'])
def index():
   pass

@app.route('/register', methods=['GET', 'POST'])
def register():
   pass

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    pass

@app.route('/signout', methods=['GET'])
def signout():
    pass

@app.route('/settings', methods=['GET', 'PATCH'])
def settings():
    pass

@app.route('/explore', methods=['GET'])
def explore():
    pass

@app.route('/search', methods=['GET', 'POST'])
def search():
    pass

@app.route('/your-music',methods=['GET', 'POST'])
def music_library():
    pass

@app.route('/song-of-the-day', methods=['GET'])
def sotd():
    pass

if __name__ == '__main__':
    app.run()
