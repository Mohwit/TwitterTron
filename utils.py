from typing import List
import json


def extract_tweets(json_string: str) -> List:
    # Parse the JSON string into a Python dictionary
    tweet_dict = json.loads(json_string)

    # Extract the values (tweets) from the dictionary
    tweets = list(tweet_dict.values())

    return tweets
