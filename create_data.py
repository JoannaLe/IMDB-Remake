 #!/usr/bin/python

import model
from model import db
from io import open
from csv import DictReader

db.drop_all()
db.create_all()

with open('data/movies.csv', 'r', encoding='utf-8-sig') as movies_file:
	reader = DictReader(movies_file)
	for row in reader:
		new_movie = model.Movie(name=row['name'], year=row['year'])

		actors = row['actors'].split(';')
		for actor in actors:
			print(actor)
			existing_actor = model.Actor.query.filter_by(name=actor).first()
			if(existing_actor):
				existing_actor.movies.append(new_movie)
				new_movie.actors.append(existing_actor)
			else:
				new_actor = model.Actor(name=actor)
				new_actor.movies.append(new_movie)
				new_movie.actors.append(new_actor)
				db.session.add(new_actor)

		db.session.add(new_movie)

with open('data/songs.csv', 'r', encoding='utf-8-sig') as songs_file:
	reader = DictReader(songs_file)
	for row in reader:
		new_song = model.Song(name=row['name'])

		# add artists
		artists = row['artists'].split(";")
		for artist_name in artists:
			print(artist_name)
			existing_artist = model.Artist.query.filter_by(name=artist_name).first()
			if(existing_artist):
				existing_artist.songs.append(new_song)
				new_song.artists.append(existing_artist)
			else:
				new_artist = model.Artist(name=artist_name)
				new_artist.songs.append(new_song)
				new_song.artists.append(new_artist)
				db.session.add(new_artist)

		# add movies
		movies = row['movies'].split(";")
		for movie_name in movies:
			print(movie_name)
			existing_movie = model.Movie.query.filter_by(name=movie_name).first()
			if(existing_movie):
				existing_movie.songs.append(new_song)
				new_song.movies.append(existing_movie)
			else:
				new_movie = model.Movie(name=movie_name)
				new_song.movies.append(new_movie)
		db.session.add(new_song)
db.session.commit()







