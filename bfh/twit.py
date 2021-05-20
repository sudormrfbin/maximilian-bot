from typing import List

import tweepy

from tcreds import CONSUMER_KEY, CONSUMER_SECRET_KEY
from tcreds import ACCESS_TOKEN, ACCESS_TOKEN_SECRET
from tcreds import BOTNAME

# Terminology
# status - tweet
# thread - series of tweets from the same user posted as a continuous stream


def construct_api() -> tweepy.API:
    # Authentication with Twitter
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    return tweepy.API(auth)


class BotMentionListener(tweepy.StreamListener):
    """
    Listens to messages that make it past the filter and handles them.
    """

    def on_status(self, status: tweepy.Status):
        """
        Executed when a new tweet is posted.
        """
        if not (status.in_reply_to_status_id and self.is_bot_mentioned(status)):
            return

        thread = Thread.from_tweet(
            self.api, self.api.get_status(status.in_reply_to_status_id)
        )
        thread.send_as_direct_messages(status.user.id)

    def is_bot_mentioned(self, status: tweepy.Status) -> bool:
        """
        Check if a tweet has mentioned our bot by @'ing.
        """
        return any(
            filter(
                lambda u: u["screen_name"] == BOTNAME, status.entities["user_mentions"]
            )
        )


class Thread:
    """
    Represents a thread from a user. Stores only the last tweet in the thread.
    """

    def __init__(self, api: tweepy.API, last_status: tweepy.Status):
        self.api = api
        # In a thread every tweet by the authour is a reply to the previous
        # tweet in the thread. Storing the last tweet is easier since every
        # tweet has the id of the tweet it replies to -- so all we have to do
        # is work backwards.
        self.last_status = last_status
        self.author = last_status.user.id
        self.thread: List[tweepy.Status] = []

        self.load_thread()

    def load_thread(self):
        # only get tweets if not already done so
        if self.thread:
            return

        # get full text of the tweet
        status = self.api.get_status(self.last_status.id, tweet_mode="extended")
        self.thread.append(status)

        while True:
            # empty string if not reply
            if status.in_reply_to_status_id_str:
                prev = self.api.get_status(
                    status.in_reply_to_status_id, tweet_mode="extended"
                )
                if prev.user.id == self.author:
                    status = prev
                    # we're traversing back up the thread from the end but need
                    # it from the front
                    self.thread.insert(0, status)
                else:
                    break
            else:
                break

    @classmethod
    def from_tweet(cls, api: tweepy.API, status: tweepy.Status):
        """
        Construct a Thread object from any tweet that is part of the thread
        itself, i.e. find the beginning of the thread given any tweet in
        between.
        """
        author = status.user.id

        for tweet in api.user_timeline(id=author, since_id=status.id):
            if tweet.in_reply_to_status_id_str == status.id_str:
                status = tweet
            else:
                break

        return cls(api, status)

    def send_as_direct_messages(self, recipient_id):
        for tweet in self.thread:
            try:
                text = tweet.full_text
            except AttributeError:
                text = tweet.text

            self.api.send_direct_message(recipient_id, text)

    def __iter__(self):
        """
        Make this object iterable using a for loop, yielding individual
        statuses.
        """
        yield from self.thread
