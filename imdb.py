from flask import Flask, request, redirect, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from model import app, db, Movie, Song
import os
# from app import app, models, db
# from app.models import Movie

db.create_all()
# os.system('python create_data.py')

@app.route('/', methods=['GET'])
def home():
	# query all movies
	movies = Movie.query.all()
	songs = Song.query.all()
	return render_template('home.html', movies=movies, songs=songs)

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

@app.route('/search/', methods=['GET'])
def search():
	actor_name = request.args['actor-input']
	movies = Actor.query.filter_by(name=actor_name)
	
	return render_template("home.html", data=movies)
