
import csv
import tweepy
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# Oauth keys
consumer_key = "Pemp33MJp1OTZLGPmHELMDVpB"
consumer_secret = "D4r1L9JA5QV71IvICITy6nxcOacd0fz1kpvbEN7yBBVSZB3H1s"
access_token = "1393867050632716289-NcLRriTJguGqhYWlTM1hy91ZePTmQh"
access_token_secret = "bnhvctZSfm7AwKMZWBkkRE25gupQiGnXCsk2S16K1nRil"

# Authentication with Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# update these for the tweet you want to process replies to 'name' = the account username and you can find the tweet id within the tweet URL
name = 'narendramodi'
tweet_id = '1393812701852303360'

replies=[]
for tweet in tweepy.Cursor(api.search,q='to:'+name, result_type='recent', timeout=999999).items(1000):
    if hasattr(tweet, 'in_reply_to_status_id_str'):
        if (tweet.in_reply_to_status_id_str==tweet_id):
            replies.append(tweet)
    print(tweet)

with open('replies_clean.csv', 'w') as f:
    csv_writer = csv.DictWriter(f, fieldnames=('user', 'text'))
    csv_writer.writeheader()
    for tweet in replies:
        row = {'user': tweet.user.screen_name, 'text': tweet.text.replace('\n', ' ')}
        csv_writer.writerow(row)