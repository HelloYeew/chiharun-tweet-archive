import tweepy
import json
import os
import urllib.request

# Warning! Very dirty code
#
# This code can update latest tweet from user up to 3250 tweet due to limitation on Twitter
# API (If you want to fetch more than 3250 tweet you must let account owner accept your API)

# Due to a problem about tweepy, I can print a video detail in tweet but cannot use it to do like download or do
# something because an Attribute error has occurred when I use extended_entities to do more than just print (Cannot
# convert to string to) but it have video information in JSON so it's just a link (Sad).

# Consumer keys and access tokens, used for OAuth
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)
tweet_number = 1
json_list = list()
for status in tweepy.Cursor(api.user_timeline, screen_name='@c_hokaze227', tweet_mode="extended").items():
    tweet_create = status.created_at
    tweet_id = status.id
    tweet_truncated = status.truncated
    tweet_text = status.full_text
    tweet_hashtags = status.entities["hashtags"]
    tweet_symbols = status.entities["symbols"]
    tweet_user_mentions = status.entities["user_mentions"]
    tweet_url_in_tweet = status.entities["urls"]
    media_text = ""
    video_text = ""
    media_number = 1
    try :
        for media in status.entities["media"]:
            media_text += f"{media_number}.\n"
            tweet_id = media["id"]
            media_text += f"Media ID : {tweet_id}\n"
            tweet_media_url = media["media_url_https"]
            if "jpg" in tweet_media_url:
                urllib.request.urlretrieve(tweet_media_url, f"{os.getcwd()}/chiharun_tweet_media/{tweet_number}_{media_number}.jpg")
            elif "jpeg" in tweet_media_url:
                urllib.request.urlretrieve(tweet_media_url, f"{os.getcwd()}/chiharun_tweet_media/{tweet_number}_{media_number}.jpeg")
            elif "png" in tweet_media_url:
                urllib.request.urlretrieve(tweet_media_url, f"{os.getcwd()}/chiharun_tweet_media/{tweet_number}_{media_number}.png")
            elif "gif" in tweet_media_url:
                urllib.request.urlretrieve(tweet_media_url, f"{os.getcwd()}/chiharun_tweet_media/{tweet_number}_{media_number}.gif")
            media_text += f"URL : {tweet_media_url}\n"
            tweet_expanded_url = media["expanded_url"]
            media_text += f"Expanded URL : {tweet_media_url}\n"
            tweet_type = media["type"]
            media_text += f"Type : {tweet_type}\n"
            media_number += 1
    except :
        media_text = None
    tweet_source = status.source
    tweet_in_reply_to_status_id = status.in_reply_to_status_id
    tweet_in_reply_to_user_id = status.in_reply_to_user_id
    tweet_in_reply_to_screen_name = status.in_reply_to_screen_name
    write_text = f"Tweet #{tweet_number}\nCreate time : {tweet_create}\nTweet ID : {tweet_id}\nTruncated : {tweet_truncated}" \
                 f"\nTweet text : {tweet_text}\nHashtags : {tweet_hashtags}\nSymbols : {tweet_symbols}\n" \
                 f"User mentions : {tweet_user_mentions}\nURL in tweet : {tweet_url_in_tweet}\n" \
                 f"Media in this tweet :\n{media_text}\nTweet Source : {tweet_source}\n" \
                 f"Tweet in reply to status ID : {tweet_in_reply_to_status_id}\n" \
                 f"Tweet in reply to user ID : {tweet_in_reply_to_user_id}\n" \
                 f"Tweet in reply to screen name : {tweet_in_reply_to_screen_name}\n"
    print(write_text)
    print()
    print("Put tweet in text file...")
    with open('chiharun_tweet_text.txt', 'a') as filehandle:
        filehandle.writelines(f"\n{write_text}")
    print(f"Write Tweet #{tweet_number} complete in {os.getcwd()}/chiharun_tweet.txt")
    print()
    json_str = json.dumps(status._json, ensure_ascii=False, indent=4)
    print("Put tweet as JSON...")
    with open(f'chiharun_tweet_json/chiharun_tweet_{tweet_number}.json', 'a') as filehandle:
        filehandle.writelines(json_str)
    print(f"Write Tweet #{tweet_number} complete in {os.getcwd()}/chiharun_tweet_json/chiharun_tweet_{tweet_number}.json")
    with open('chiharun_tweet_one_file.json', 'a') as filehandle:
        filehandle.writelines(f"{json_str},\n")
    print(f"Write Tweet #{tweet_number} complete in {os.getcwd()}/chiharun_tweet_one_file.json")
    print()
    print(f"Tweet #{tweet_number} import complete!")
    tweet_number += 1

print("Complete!")


