import json
import csv
import tweepy
import re
import io
import my_twitter_credentials

consumer_key= my_twitter_credentials.CONSUMER_KEY
consumer_secret= my_twitter_credentials.CONSUMER_SECRET
access_token= my_twitter_credentials.ACCESS_TOKEN
access_token_secret= my_twitter_credentials.ACCESS_TOKEN_SECRET

"""
INPUTS:
    consumer_key, consumer_secret, access_token, access_token_secret: codes
    telling twitter that we are authorized to access this data
    hashtag_phrase: the combination of hashtags to search for
OUTPUTS:
    none, simply save the tweet info to a spreadsheet
"""

def search_for_hashtags(consumer_key, consumer_secret, access_token, access_token_secret, hashtag_phrase):
    # Twitter authentication and the connection to Twitter API
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    # Initializing Tweepy API
    api = tweepy.API(auth, wait_on_rate_limit=True)
    # Name of csv file to be created
    fname = "17thjune"
    # Open the spreadsheet
    with open('%s.csv' % (fname), 'w', encoding="utf-8") as file:
        w = csv.writer(file)
        # Write header row (feature column names of your choice)
        w.writerow(['timestamp', 'tweet_text', 'username', 'all_hashtags', 'location', 'followers_count', 'retweet_count', 'favorite_count'])
        # For each tweet matching our hashtags, write relevant info to the spreadsheet
        for tweet in tweepy.Cursor(api.search, q=hashtag_phrase+' -filter:retweets', lang="en", tweet_mode='extended').items(99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999):
            w.writerow([tweet.created_at, tweet.full_text.replace('\n',' ').encode('utf-8'), tweet.user.screen_name.encode('utf-8'), [e['text'] for e in tweet._json['entities']['hashtags']],  tweet.user.location, tweet.user.followers_count, tweet.retweet_count, tweet.favorite_count])

hashtag_phrase= "edchat"

if __name__ == '__main__':
    search_for_hashtags(consumer_key, consumer_secret, access_token, access_token_secret, hashtag_phrase)
