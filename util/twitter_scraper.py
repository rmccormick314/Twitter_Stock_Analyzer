# IMPORTS & DEPENDENCIES =======================================================
import tweepy
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from twitter_auth import create_auth

# DECLARE VARIABLES ============================================================
"""Secret file containing API keys & tokens"""
secret_file = "twitter-keys.txt"

"""VADER Sentiment Intensity Analyzer"""
sid = SentimentIntensityAnalyzer()

api = create_auth()

# FUNCTION DECLARATIONS ========================================================
def get_sentiment(searchterm, n):
    """Searches Twitter for given term."""
    sentiment = 0;

    # Searches for Tweets matching query.
    public_tweets = api.search_tweets(q=searchterm,
                                      count=n+1,
                                      lang='en',
                                      tweet_mode="extended")

    # For each tweet, get full text and analyze sentiment.
    for tweet_info in public_tweets:
        tweet=tweet_info.full_text

        print(sid.polarity_scores(tweet))
        sentiment += sid.polarity_scores(tweet)['compound']

    # Calculate average sentiment of all tweets and return.
    sentiment = sentiment / n
    print("Average sentiment on Twitter for " + searchterm + " is: " + str(sentiment))
    return sentiment
