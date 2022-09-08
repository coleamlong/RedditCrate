import imp
import spotipy
from spotipy import util

PLAYLIST_NAME = 'RedditCrate'
PLAYLIST_DESC = 'This is RedditCrate!'
USERNAME = 'RedditCrateBackend'
SCOPE = 'playlist-modify-private'

CLIENT_ID = "91d037f7894441b2aab67c0acec6689d"
CLIENT_SECRET = "36f5c2a0073943ab9f12953844bb44cf"
REDIRECT_URI = "https://localhost:8888/callback"


class Client():
    def __init__(self) -> None:
        token = util.prompt_for_user_token(
            USERNAME, 
            SCOPE, 
            CLIENT_ID, 
            CLIENT_SECRET, 
            REDIRECT_URI)

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
