from __future__ import print_function
from flask import Flask, request, redirect, render_template, session, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from model import app, db, login, Movie, Song, User
from forms import LoginForm, RegistrationForm
import os, sys

@app.route('/', methods=['GET'])
def home():
	# query all movies and songs
	movies = Movie.query.all()
	songs = Song.query.all()
	return render_template('home.html', movies=movies, songs=songs)

@app.route('/login/', methods=['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		session['username'] = request.form['username']
		flash('Login requested for user {}'.format(form.username.data))
		return redirect('/')
	return render_template('login.html', form=form)

@app.route('/signup', methods=['GET','POST'])
def signup():
	# validate registration info and create new user
	form = RegistrationForm()
	if request.method == 'POST' and form.validate():
		new_user = User(username=form.username.data)
		new_user.set_password(form.password.data)
		db.session.add(new_user)
		flash('Registration Successful.')
		return redirect(url_for('login'))
	# get request for registration page
	return render_template('register.html', form=form)

@app.route('/search/', methods=['GET'])
def search():
	song_name = request.args['song-input']
	song = Song.query.filter_by(name=song_name).first()

	if song is None:
		return render_template("not_found.html")

	# { artist : list of (song, artists, movies)}
	data = {}
	for artist in song.artists:
		items = []
		for s1 in artist.songs:
			if s1.name == song_name:
				items.insert(0, (s1.name, [artist.name for artist in s1.artists], [movie.name for movie in s1.movies]))
			else:
				items.append((s1.name, [artist.name for artist in s1.artists], [movie.name for movie in s1.movies]))
			print((s1.name, [artist.name for artist in s1.artists], [movie.name for movie in s1.movies]), file=sys.stderr)
		data[artist] = items
	
	return render_template("results.html", data=data, search_term=song_name)

# go to movie details page
@app.route('/details/<movie>/', methods=['GET'])
def details(movie):
  return render_template("details.html", year=data[movie][0], actors=data[movie][1], movie=movie)

@app.route('/add/',  methods=['GET'])
def add():
	return render_template("add.html", data=data)

@app.route('/update/',  methods=['POST'])
def update():
	return render_template("update.html", data=data)

@app.route('/update/update/<id>',  methods=['GET'])
def new_update():
	oldMovie = Movie.query.filter_by(movie_id=id)
	if(request.args['movie-update']):
		movie = request.args['movie-update']
		oldMovie.update(name=movie)
	if(request.args['year-update']):
		year = request.args['year-update']
		oldMovie.update(year=year)
	if(request.args['actors-update']):
		actors = request.args['actors-update']
		for actor_name in actors.split():
			actor_name = actor_name.rstrip()
			Actor.query.filter_by(name=actor_name).update(movies.append(oldMovie))

	db.session.commit()
	return render_template("update.html", data=data)

@app.route('/add/song',  methods=['GET'])
def add_song():
	return render_template("add-song.html", data=data)

@app.route('/add/new/', methods=['GET'])
def new_movie():
	movie = request.args['movie']
	year = request.args['year']
	actors = request.args['actors']
	data[movie] = [year, actors.split(',')]

	newMovie = Movie(name=movie, year=year)
	for actor in actors.split():
		actor = actor.rstrip()
		newActor = Actor(name=actor, movies=[newMovie])
		db.session.add(newActor)
	db.session.add(newMovie)
	db.session.commit()
	return render_template('home.html', data=data)

@app.route('/delete/<movie>', methods=['GET'])
def delete(movie):
	movie = Movie.query.filter_by(name=movie)
	db.session.delete(movie)
	db.session.commit()

	return render_template('home.html', data=data)

# @app.route('/deleteActor/', methods=['GET'])
# def deleteActor():
# 	actor_name = request.args['actor-input']
# 	actor = Actor.query.filter_by(name=actor_name)
# 	db.session.delete(actor)
# 	db.session.commit()
# 	return render_template('home.html', data=data)