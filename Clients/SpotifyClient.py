import spotipy
from spotipy.oauth2 import SpotifyOAuth

PLAYLIST_NAME = 'RedditCrate'
PLAYLIST_DESC = 'This is RedditCrate!'
USERNAME = 'nightcorepm'

class Client():
    def __init__(self) -> None:
        self.spotify = spotipy.Spotify(
            client_credentials_manager=SpotifyOAuth(
                client_id="91d037f7894441b2aab67c0acec6689d",
                client_secret="36f5c2a0073943ab9f12953844bb44cf",
                scope="playlist-modify-private",
                redirect_uri="https://localhost:8888/callback",
            )
        )

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
            user=USERNAME,
            name=PLAYLIST_NAME,
            public=public,
            description=PLAYLIST_DESC            
        )['id']
    

    def add_tracks_to_playlist(self, playlist_id, tracks):
        return self.spotify.user_playlist_add_tracks(
            user=USERNAME,
            playlist_id=playlist_id,
            tracks=tracks
        )
