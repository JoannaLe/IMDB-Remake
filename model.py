from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.config.from_object(Config)
print('***CONFIGURED**')
db = SQLAlchemy(app)
login = LoginManager(app)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

actor2movie = db.Table('actor2movie',
	db.Column('actor.id', db.Integer, db.ForeignKey('actor.actor_id')),
	db.Column('movie_id', db.Integer, db.ForeignKey('movie.movie_id'))
)

song2movie = db.Table('song2movie',
	db.Column('song.id', db.Integer, db.ForeignKey('song.song_id')),
	db.Column('movie_id', db.Integer, db.ForeignKey('movie.movie_id'))
)

artist2song = db.Table('artist2song',
	db.Column('artist.id', db.Integer, db.ForeignKey('artist.artist_id')),
	db.Column('song_id', db.Integer, db.ForeignKey('song.song_id'))
)

class Actor(db.Model):
	actor_id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20))
	movies = db.relationship('Movie', secondary=actor2movie, backref=db.backref('actor-movies', lazy='dynamic'))

	def __repr__(self):
		return '<User {}>'.format(self.name)

class Movie(db.Model):
	movie_id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20))
	year = db.Column(db.Integer)
	actors = db.relationship('Actor', secondary=actor2movie, backref=db.backref('movie-actors', lazy='dynamic'))
	songs = db.relationship('Song', secondary=song2movie, backref=db.backref('movie-songs', lazy='dynamic'))

class Song(db.Model):
	song_id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20))
	artists = db.relationship('Artist', secondary=artist2song, backref=db.backref('song-artists', lazy='dynamic'))
	movies = db.relationship('Movie', secondary=song2movie, backref=db.backref('song-movies', lazy='dynamic'))
	image = db.Column(db.String(200))

class Artist(db.Model):
	artist_id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20))
	songs = db.relationship('Song', secondary=artist2song, backref=db.backref('artist-songs', lazy='dynamic'))

class User(UserMixin, db.Model):
	user_id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20))
	email = db.Column(db.String(40))
	password_hash = db.Column(db.String(128))
	# songs = db.Column()
	def set_password(self, password):
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)
