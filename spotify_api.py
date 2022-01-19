import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

def api_call(search=None, artist=None, album=None, track=None):
    try:
        if search:
            return "success", spotify.search(q='artist:' + search, type='artist')

        if artist:
            return "success", spotify.artist_albums(artist, album_type='album')
        
        if album:
            return "success", spotify.album_tracks(album)
        
        if track:
            return "success", spotify.audio_analysis(track)
        return "success", []
    except spotipy.exceptions.SpotifyException as e:
        return "Spotify api failed : error code "+ e.code, []
    except Exception as e:
        return "Some error occurred - please contact admin  "+ e, [] 
