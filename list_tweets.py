import os
import tweepy

consumer_key = os.environ["TWITTER_API_KEY"]
consumer_secret = os.environ["TWITTER_API_SECRET"]
access_token = os.environ["TWITTER_ACCESS_TOKEN"]
access_token_secret = os.environ["TWITTER_ACCESS_TOKEN_SECRET"]

# AUTHENTICATE

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# INITIALIZE API CLIENT

api = tweepy.API(auth)

# ISSUE REQUESTS

user = api.me() # get information about the currently authenticated user

tweets = api.user_timeline() # get a list of tweets posted by the currently authenticated user

# PARSE RESPONSES

print("---------------------------------------------------------------")
print("LIST OF @{0}'s RECENT TWEETS (FOLLOWERS: {1} / FOLLOWING: {2}):".format(user.screen_name, user.followers_count, user.friends_count))
print("---------------------------------------------------------------")

for tweet in tweets:
    created_on = tweet.created_at.strftime("%d-%m-%Y")
    print(" -- ", created_on, tweet.text)
