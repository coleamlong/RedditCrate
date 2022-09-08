import os
import praw
import re

TITLE_DELIMITERS = " -- ", " - ", " ["

class Client():
    def __init__(self) -> None:
        self.reddit = praw.Redd(
            client_id=os.getenv('redditClientId'),
            client_secret=os.getenv('redditClientSecret'),
            password= os.getenv('redditPassword'),
            user_agent=os.getenv('redditUserAgent'),
            username=os.getenv('redditPassword'),
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
