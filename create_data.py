import model
from model import db

db.drop_all()
db.create_all()

data = {
	'Crazy Rich Asians' : [2018, ['Constance Wu', 'Henry Golding', 'Michelle Yeoh']],
	'La La Land' : [2016, ['Ryan Gosling', 'Emma Stone']],
	'Harry Potter and the Sorcerer\'s Stone' : [2001, ['Daniel Radcliffe', 'Rupert Grint', 'Emma Watson']],
	'Kung Fu Panda' : [2008, ['Jack Black', 'Ian McShane', 'Angelina Jolie']],
	'Frozen' : [2013, ['Kristen Bell', 'Idina Menzel', 'Jonathan Groff']],
	'Madagascar' : [2005, ['Chris Rock', 'Ben Stiller', 'David Schwimmer']],
	'Despicable Me' : [2010, ['Steve Carell', 'Jason Segel', 'Russell Brand']],
	'Beauty and the Beast' : [2017, ['Emma Watson', 'Dan Stevens', 'Luke Evans']],
	'Dear Evan Hansen' : [2016, ['Ben Platt', 'Laura Dreyfuss', 'Rachel Bay Jones']]
}

songs = {
	'Let It Go' : {
	'artists' : ['Idina Menzel'],
	'movies' : ['Frozen'],
	'image': 'https://images-na.ssl-images-amazon.com/images/I/61gYerL61JL._SS500.jpg'
	},
	'Somewhere in the Crowd' : {
	'artists' : ['Emma Stone'],
	'movies' : ['La La Land'],
	'image' : 'https://upload.wikimedia.org/wikipedia/en/thumb/8/83/La_La_Land_soundtrack.jpg/220px-La_La_Land_soundtrack.jpg'
	},
	'City of Stars' : {
	'artists' : ['Emma Stone', 'Ryan Gosling'],
	'movies' : ['La La Land'],
	'image' : 'https://upload.wikimedia.org/wikipedia/en/thumb/8/83/La_La_Land_soundtrack.jpg/220px-La_La_Land_soundtrack.jpg'
	},
	'Can\'t Help Falling in Love' : {
	'artists' : ['Kina Grannis'],
	'movies' : ['Crazy Rich Asians'],
	'image' : 'https://i.ytimg.com/vi/GR6L_C0Ii6s/maxresdefault.jpg'
	},
	'Sweet Home Alabama' : {
	'artists' : ['Lynyrd Skynyrd'],
	'movies' : ['Despicable Me', 'Forrest Gump'],
	'image' : 'https://img.discogs.com/TUwRx5jpVf0EgCIsGdqGEhO9j64=/fit-in/600x600/filters:strip_icc():format(jpeg):mode_rgb():quality(90)/discogs-images/R-7800158-1449031512-4317.jpeg.jpg'
	},
	'Kung Fu Fighting' : {
	'artists' : ['Carl Douglas'],
	'movies' : ['Kung Fu Panda', 'Rush Hour 3'],
	'image' : 'https://img.discogs.com/j8Y-Y39_7ZqvjXr49Reop_rYNkQ=/fit-in/600x600/filters:strip_icc():format(jpeg):mode_rgb():quality(90)/discogs-images/R-5375146-1397606049-7965.png.jpg'
	},
	'Stayin\' Alive' : {
	'artists' : ['The Bee Gees'],
	'movies' : ['Madagascar', 'Saturday Night Fever'],
	'image' : 'https://upload.wikimedia.org/wikipedia/en/thumb/3/36/Bee_Gees_Stayin_Alive.jpg/220px-Bee_Gees_Stayin_Alive.jpg'
	},
	'What a Wonderful World' : {
	'artists' : ['Louie Armstrong', 'Israel Kamakawiwo\'ole'],
	'movies' : ['Madagascar', 'The Mentalist'],
	'image' : 'https://img.discogs.com/qiN8MZ-cY8C3RrBv2GHWpEKsnFM=/fit-in/600x600/filters:strip_icc():format(jpeg):mode_rgb():quality(90)/discogs-images/R-2977237-1348953297-6252.jpeg.jpg'
	},
	'For the First Time in Forever' : {
	'artists' : ['Kristen Bell', 'Idina Menzel'],
	'movies' : ['Frozen'],
	'image' : 'https://images-na.ssl-images-amazon.com/images/I/61gYerL61JL._SS500.jpg'
	},
	'How Does A Moment Last Forever' : {
	'artists' : ['Emma Watson'],
	'movies' : ['Beauty and the Beast'],
	'image' : 'https://upload.wikimedia.org/wikipedia/en/thumb/4/44/BATB_2017_Soundtrack.jpg/220px-BATB_2017_Soundtrack.jpg'
	},
	'Fools Who Dream' : {
	'artists' : ['Emma Stone'],
	'movies' : ['La La Land'],
	'image' : 'https://upload.wikimedia.org/wikipedia/en/thumb/8/83/La_La_Land_soundtrack.jpg/220px-La_La_Land_soundtrack.jpg'
	},
	'For Forever' : {
	'artists' : ['Ben Platt'],
	'movies' : ['Dear Evan Hansen'],
	'image' : 'https://images-na.ssl-images-amazon.com/images/I/81fgTw%2BSTAL._SL1430_.jpg'
	}
}

for movie, details in data.iteritems():
	new_movie = model.Movie(name=movie, year=details[0])

	for actor in details[1]:
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

for song, details in songs.iteritems():
	new_song = model.Song(name=song)

	# add artists
	for artist_name in details['artists']:
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
	for movie_name in details['movies']:
		existing_movie = model.Movie.query.filter_by(name=movie_name).first()
		if(existing_movie):
			existing_movie.songs.append(new_song)
			new_song.movies.append(existing_movie)
		else:
			new_movie = model.Movie(name=movie_name)
			new_song.movies.append(new_movie)
	db.session.add(new_song)
db.session.commit()







