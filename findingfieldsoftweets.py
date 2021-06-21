import tweepy
import pandas as pd
import sys
import my_twitter_credentials

consumer_key= my_twitter_credentials.CONSUMER_KEY
consumer_secret= my_twitter_credentials.CONSUMER_SECRET
access_token= my_twitter_credentials.ACCESS_TOKEN
access_token_secret= my_twitter_credentials.ACCESS_TOKEN_SECRET

# Twitter authentication and the connection to Twitter Streaming API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Initializing Tweepy API
api = tweepy.API(auth, wait_on_rate_limit=True)

# Streaming a tweet
cursor= tweepy.Cursor(api.user_timeline, tweet_mode="extended").items(1)

# Printing list of attributes and methods (fields) of tweet object
for i in cursor:
    print(dir(i))

# Output has been saved as text file.
