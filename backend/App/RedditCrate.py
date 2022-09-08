from Clients import SpotifyClient, RedditClient
from dotenv import load_dotenv

def main():
    load_dotenv()
    spotify = SpotifyClient.Client()
    reddit = RedditClient.Client()

    posts = reddit.get_submssions('listentothis')

    tracklist = reddit.parse_submissions(posts)

    spotify_uris = []
    for track in tracklist:
        song_uri = spotify.try_get_track_uri(track)

        if song_uri != None:
            spotify_uris.append(song_uri)

    playlist_id = spotify.create_playlist()
    spotify.add_tracks_to_playlist(playlist_id, spotify_uris)


if __name__ == "__main__":
    main()