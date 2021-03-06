import tweepy
import json
import os
import urllib.request

# Warning! Very dirty code

# Consumer keys and access tokens, used for OAuth
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

# It's but a bit so just delete a first line of a JSON file that you will get

user_data = api.get_user(screen_name='@c_hokaze227')
json_str = json.dumps(user_data._json, ensure_ascii=False, indent=4)
with open('chiharun_user_data.json', 'a') as filehandle:
    filehandle.writelines(json_str)