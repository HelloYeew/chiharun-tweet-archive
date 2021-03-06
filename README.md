# Chiharun Tweet Archive

![Chiharun_latest_album](https://static.wikia.nocookie.net/nanabunnonijyuuni/images/c/cb/Boku_ga_Motteru_Mono_Nara_Chiharu.jpg/revision/latest/scale-to-width-down/310?cb=20210122115209)

Repositories for archive Chiharun 22/7's tweet as mush as Twitter API can do.

## Detail

Because all SNS of Chiharu Hokaze will be closed in 7 March after her graduation from 22/7 so I want to archive her Twitter as mush as I can (or as much as Twitter can do).
This is a source code that I write and run to make this project work.

### Problem about Twitter API

Due to Twitter API law, if a user that you want to fetch not authorize your app in Twitter developer dashboard 
you can fetch a Tweet in that user only first 3250 Tweets. That's why I can only fetch only 3250 of total 6647 tweet. (Sad life noise)

### Running this program and what you get from these programs

It have 2 file that you can run.

- [fetch_chiharun_tweet.py](fetch_chiharun_tweet.py)
- [fetch_chiharun_user_data.py](fetch_chiharun_user_data.py)

Before you run you must put Twitter API key and make 2 directory (chiharun_tweet_json and chiharun_tweet_media) before running these 2 programs.

After you run these 2 files (before end of 7 March) you will get.

- *chiharun_tweet_json* directory : After running a program you will get a 3250 JSON file. Each file contains the latest detail about latest 3250 tweets that Chiharun tweet.
- *chiharun_tweet_media* directory : A picture from the latest 3250 tweet.
- *chiharun_tweet_text.txt* : A translation from 3250 JSON file to a text file like you read in her Twitter.
- *chiharun_tweet_one_file.json* : All file in *chiharun_tweet_json* directory but in one file LOL
- *chiharun_user_data.json* : Chiharun user data in JSON file

I will put all of this file in release page= becuase I know you cannot run these program after 7 March.

## Contribution

You don't want to contribute this repositories anymore. Just use all file that I get from her tweets to contribute in other way like make website that archive these tweets etc.

If you use my data please credit to this repositories. Thx!

