from typing import List

import tweepy


# Terminology
# status - tweet
# thread - series of tweets from the same user posted as a continuous stream


class BotMentionListener(tweepy.StreamListener):
    """
    Listens to messages that make it past the filter and handles them.
    """

    def on_status(self, status: tweepy.Status):
        """
        Executed when a new tweet is posted.
        """
        if status.in_reply_to_status_id:
            thread = Thread.from_tweet(
                self.api, self.api.get_status(status.in_reply_to_status_id)
            )


class Thread:
    """
    Represents a thread from a user. Stores only the last tweet in the thread.
    """

    def __init__(self, api: tweepy.api.API, last_status: tweepy.Status):
        self.api = api
        # In a thread every tweet by the authour is a reply to the previous
        # tweet in the thread. Storing the last tweet is easier since every
        # tweet has the id of the tweet it replies to -- so all we have to do
        # is work backwards.
        self.last_status = last_status
        self.thread: List[tweepy.Status] = []

        self.load_thread()

    def load_thread(self):
        # only get tweets if not already done so
        if self.thread:
            return

        status = self.last_status
        self.thread.append(status)

        while True:
            # empty string if not reply
            if status.in_reply_to_status_id_str:
                prev = self.api.get_status(status.in_reply_to_status_id)
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
    def from_tweet(cls, api: tweepy.api.API, status: tweepy.Status):
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

    def __iter__(self):
        """
        Make this object iterable using a for loop, yielding individual
        statuses.
        """
        yield from self.thread
