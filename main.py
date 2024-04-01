import tweepy
from dotenv import load_dotenv
import os

load_dotenv()
from tweets_generator import get_new_tweet, get_threads
from utils import extract_tweets

AUTHENTICATION_BEARER_TOKEN = os.getenv("AUTHENTICATION_BEARER_TOKEN")
CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")


client = tweepy.Client(
    bearer_token=AUTHENTICATION_BEARER_TOKEN,
    consumer_key=CONSUMER_KEY,
    consumer_secret=CONSUMER_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET,
)


# tweet = get_new_tweet()[:279]
# print(tweet)
# response = client.create_tweet(text=tweet)
# print(response)

## to be added
# -- Post threads ---
threads = get_threads()
tweets = extract_tweets(threads)
response = client.create_tweet(text=tweets[0])

for i in range(1, len(tweets)):
    response = client.create_tweet(
        text=tweets[i], in_reply_to_tweet_id=response.data["id"]
    )
