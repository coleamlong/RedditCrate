from collections import namedtuple
import spotipy
import praw
from spotipy.oauth2 import SpotifyOAuth

import re

reddit = praw.Reddit(
    client_id="fzLYV7zZWuvpfADxIGiUmA",
    client_secret="tpKuhof3MKuXXnKfpR7tVuOIXM1UXQ",
    password="HighJockey664!",
    user_agent="LAPTOP",
    username="MeatSuccessful",
)

spotify = spotipy.Spotify(
    oauth_manager=SpotifyOAuth(
        client_id="91d037f7894441b2aab67c0acec6689d",
        client_secret="36f5c2a0073943ab9f12953844bb44cf",
        scope="playlist-modify-private",
        redirect_uri="https://localhost:8888/callback"
    )
)

submissions = reddit.subreddit('listentothis').hot(limit=25)

delimiters = " -- ", " - ", " ["
regex_pattern = '|'.join(map(re.escape, delimiters))

Song = namedtuple("Song", ["name", "artist"])
song_list = []
for submission in submissions:
    if submission.title == 'Music Melting Pot [Week of September 05, 2022]':
        continue

    tokens = re.split(regex_pattern, submission.title)
    new_song = Song(name=tokens[1], artist=tokens[0])
    song_list.append(new_song)

spotify_uris = []
for song in song_list:
    search_result = spotify.search(q=f'track:{song.name}, artist:{song.artist}', type="track")
    if search_result['tracks']['total'] != 0:
        track = search_result['tracks']['items'][0]
        spotify_uris.append(track['uri'])

playlist = spotify.user_playlist_create('nightcorepm', 'RedditCrate', False, False, 'This is RedditCrate!')
response = spotify.user_playlist_add_tracks('nightcorepm', playlist_id=playlist['id'], tracks=spotify_uris, position=None)
