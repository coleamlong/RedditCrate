import praw
import re

TITLE_DELIMITERS = " -- ", " - ", " ["

class Client():
    def __init__(self) -> None:
        self.reddit = praw.Reddit(
            client_id="fzLYV7zZWuvpfADxIGiUmA",
            client_secret="tpKuhof3MKuXXnKfpR7tVuOIXM1UXQ",
            password="HighJockey664!",
            user_agent="LAPTOP",
            username="MeatSuccessful",
        )


    def get_submssions(self, subreddit, limit=10):
        return self.reddit.subreddit(subreddit).hot(limit=limit)

    def parse_submissions(self, submissions):
        regex_pattern = '|'.join(map(re.escape, TITLE_DELIMITERS))

        tracklist = []

        for submission in submissions:
            if submission.title == 'Music Melting Pot [Week of September 05, 2022]':
                continue

            tokens = re.split(regex_pattern, submission.title)
            new_song = [tokens[1], tokens[0]]
            tracklist.append(new_song)

        return tracklist
