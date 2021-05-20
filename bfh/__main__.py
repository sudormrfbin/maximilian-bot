import logging

import tweepy

from twit import construct_api, BotMentionListener
from tcreds import BOTNAME

logger = logging.getLogger('bfh')
logger.setLevel(logging.DEBUG)
sh = logging.StreamHandler()
sh.setLevel(logging.DEBUG)
fh = logging.FileHandler('bfh.log')
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    "%(asctime)s:%(name)s: %(message)s (%(levelname)s)", "%H:%M:%S"
)
sh.setFormatter(formatter)
fh.setFormatter(formatter)
logger.addHandler(sh)
logger.addHandler(fh)

api = construct_api()
streamlistener = BotMentionListener(api=api)
stream = tweepy.Stream(auth=api.auth, listener=streamlistener)

logger.debug(f"Listening for tweets containing '{BOTNAME}'")
stream.filter(track=[BOTNAME])
