import os
import spotipy
from spotipy import util

PLAYLIST_NAME = 'RedditCrate'
PLAYLIST_DESC = 'This is RedditCrate!'

class Client():
    def __init__(self) -> None:
        token = util.prompt_for_user_token(
            username=os.getenv('spotifyUsername'), 
            scope='playlist-modify-private', 
            client_id=os.getenv('spotifyClientId'), 
            client_secret=os.getenv('spotifyClientSecret'), 
            redirect_uri=os.getenv('spotifyRedirectUri')
        )

        if token:
            self.spotify = spotipy.Spotify(
                auth=token)
        else:
            print("Couldn't get user token.")

    def try_get_track_uri(self, track):
        search_result = self.spotify.search(
            q=f'track:{track[0]}, artist:{track[1]}',
            type='track'
        )

        if search_result['tracks']['total'] == 0:
            return None
        
        track = search_result['tracks']['items'][0]
        print(track['uri'])
        return track['uri']


    def create_playlist(self, public=False) -> str:
        return self.spotify.user_playlist_create(
            user=self.spotify.me()['id'],
            name=PLAYLIST_NAME,
            public=public,
            description=PLAYLIST_DESC            
        )['id']
    

    def add_tracks_to_playlist(self, playlist_id, tracks):
        return self.spotify.user_playlist_add_tracks(
            user=self.spotify.me()['id'],
            playlist_id=playlist_id,
            tracks=tracks
        )
