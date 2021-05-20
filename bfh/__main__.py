import tweepy

from twit import construct_api, BotMentionListener
from tcreds import BOTNAME


api = construct_api()
streamlistener = BotMentionListener(api=api)
stream = tweepy.Stream(auth=api.auth, listener=streamlistener)
stream.filter(track=[BOTNAME])
