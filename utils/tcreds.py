# variables that contain the credentials to access the twitter api.

import os

from dotenv import load_dotenv

load_dotenv()

CONSUMER_KEY = os.getenv("TWITTER_API_KEY", "")
CONSUMER_SECRET_KEY = os.getenv("TWITTER_API_SECRET_KEY", "")

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN", "")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET", "")
