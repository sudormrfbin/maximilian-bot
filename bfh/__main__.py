import csv
import tweepy
import ssl

from tcreds import CONSUMER_KEY, CONSUMER_SECRET_KEY
from tcreds import ACCESS_TOKEN, ACCESS_TOKEN_SECRET

ssl._create_default_https_context = ssl._create_unverified_context

# Authentication with Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# update these for the tweet you want to process replies to
# 'name' = the account username
# you can find the tweet id within the tweet URL
name = "narendramodi"
tweet_id = "1393812701852303360"

replies = []
for tweet in tweepy.Cursor(
    api.search, q=f"to:{name}", result_type="recent", timeout=999999
).items(1000):
    if hasattr(tweet, "in_reply_to_status_id_str"):
        if tweet.in_reply_to_status_id_str == tweet_id:
            replies.append(tweet)
    print(tweet)

with open("replies_clean.csv", "w") as f:
    csv_writer = csv.DictWriter(f, fieldnames=("user", "text"))
    csv_writer.writeheader()
    for tweet in replies:
        row = {"user": tweet.user.screen_name, "text": tweet.text.replace("\n", " ")}
        csv_writer.writerow(row)
