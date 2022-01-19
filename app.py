from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from spotify_api import api_call

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def search_artist():
    artists = []
    if request.method == 'POST':
        search_string = request.form.get("artist")
        spotify_msg, results = api_call(search=search_string)
        items = results['artists']['items']
        for item in items:
            artist = {"key": item['name'], "value": item['uri'], "image": item['images'][0]['url']}
            artists.append(artist)

        return render_template('index.html', artists=artists, albums=[], songs=[], song={}, msg=spotify_msg, heading=search_string)
    return render_template('index.html', artists=[], albums=[], songs=[], song={}, msg=None)

@app.route("/artist/<heading>/<uri>")
def get_artist_albums(heading, uri):
    albums = []
    spotify_msg, results = api_call(artist=uri)
    items = results['items']
    for item in items:
        album = {"key": item['name'], "value": item['uri'], "image": item['images'][0]['url']}
        albums.append(album)
    return render_template('index.html', artists=[], albums=albums, songs=[], song={}, msg=spotify_msg, heading=heading)

@app.route("/album/<heading>/<uri>")
def get_album_tracks(heading, uri):
    tracks = []
    spotify_msg, results = api_call(album=uri)
    items = results['items']
    for item in items:
        track = {"key": item['name'], "value": item['uri']}
        tracks.append(track)
    return render_template('index.html', artists=[], albums=[], songs=tracks, song={}, msg=spotify_msg, heading=heading)

@app.route("/track/<heading>/<uri>")
def get_track_info(heading, uri):
    spotify_msg, results = api_call(track=uri)
    return render_template('index.html', artists=[], albums=[], songs=[], song=results['track'], msg=spotify_msg, heading=heading)

if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.run()