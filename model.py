from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

actor2movie = db.Table('actor2movie',
	db.Column('actor.id', db.Integer, db.ForeignKey('actor.actor_id')),
	db.Column('movie_id', db.Integer, db.ForeignKey('movie.movie_id'))
)

class Actor(db.Model):
	actor_id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20))
	movies = db.relationship('Movie', secondary=actor2movie, backref=db.backref('movies', lazy='dynamic'))

	def __repr__(self):
		return '<User {}>'.format(self.name)

class Movie(db.Model):
	movie_id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20))
	year = db.Column(db.Integer)