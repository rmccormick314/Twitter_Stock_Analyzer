# IMPORTS & DEPENDENCIES =======================================================
import tweepy
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from auth import create_auth

# DECLARE VARIABLES ============================================================
"""Secret file containing API keys & tokens"""
secret_file = "twitter-keys.txt"

"""VADER Sentiment Intensity Analyzer"""
sid = SentimentIntensityAnalyzer()

"""Creates authenicated API object from file"""
api = create_auth()

# FUNCTION DECLARATIONS ========================================================
class SentimentSearcher:
    # Function Name: __init__
    # Function     : Initializes the sentiment search object
    # Inputs       : Key-word arguments - n_searches (int), language (str),
    #                                     logging (bool)
    # Outputs      : None
    # Dependencies : None
    def __init__( self, **kwargs ):
        """Set defaults for search object"""
        kwargs.setdefault( "n_searches", 100 )   # Number of searches per scrape
        kwargs.setdefault( "language", "en" )    # Language to search in
        kwargs.setdefault( "logging", True )     # Log to monitor or no

        """Set attributes by keyword if necessary"""
        for key, value in kwargs.items():
            setattr( self, key, value )

    # Function Name: sentiment_by_term
    # Function     : Gets average compound sentiment from a searchterm
    # Inputs       : Searchterm (str)
    # Outputs      : Average Sentiment (int)
    # Dependencies : Tweepy
    def sentiment_by_term( searchterm ):
        """Establish return variable"""
        sentiment = 0;

        """Searches for Tweets matching query"""
        public_tweets = api.search_tweets( q = searchterm,
                                           count = self.n_searches,
                                           lang = self.language,
                                           tweet_mode = "extended" )

        """For each tweet, get full text and analyze sentiment"""
        for tweet_info in public_tweets:
            tweet=tweet_info.full_text

            if( self.logging == True ):
                print(sid.polarity_scores(tweet))
            sentiment += sid.polarity_scores(tweet)['compound']

        """Calculate average sentiment of all tweets and return"""
        sentiment = sentiment / n

        """Print the sentiment to screen if logging is on"""
        if( self.logging == True ):
            print( "Average sentiment on Twitter for " + \
                    searchterm + " is: " + str(sentiment) )

        """Return average compound sentiment"""
        return sentiment
