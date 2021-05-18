# tinkerhub-bfh-py-twitter
Twitter bot in Python for TinkerHub BFH

## Setup

Set required tokens in [`.env`](./.env) file in the root of the project (Do NOT commit this file to git).

Make a virtual environment, and then install dependencies with
`pip install -r requirements.txt`.

To run the project from the root:

```bash
python3 bfh
```

## Overview

1. User makes account in our webapp
2. (Optional) User's twitter account connected with our webapp for getting user specific [access token](https://docs.tweepy.org/en/v3.10.0/auth_tutorial.html)
3. User mentions our bot under a twitter thread
4. Bot listens for mentions using [streaming API](https://docs.tweepy.org/en/v3.10.0/streaming_how_to.html)
5. Bot saves thread to database with user's name
6. User logs in to our webapp and sees saved threads
7. (Optional) User downloads tweets in pdf or text

## Summary

Twitter has many great people sharing valuable information in the form of
threads. Write a personal script that uses the Twitter API to save the tweet
thread in a suitable form for later consumption (maybe PDF or text file or a
table view). User should be able to log in to a dashboard and access saved
threads.

## Elements

1. Access Twitter API using Python
2. Transform the tweets into .txt or pdf format using Python libraries
3. A simple user management system

## Acceptance criteria

- Able to tag the bot on a twitter thread
- Able to access saved twitter threads
