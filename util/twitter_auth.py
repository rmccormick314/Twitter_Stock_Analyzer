# IMPORTS & DEPENDENCIES =======================================================
import tweepy

# DECLARE VARIABLES ============================================================
## Secret file containing Twitter authentication stuff
secret_file = "twitter-keys.txt"

# READ API KEYS & TOKENS =======================================================
def create_auth():
    """Read through the secret file"""
    with open(secret_file) as f:
        lines = f.readlines()

    """Assign each item to its value in the file"""
    twitter_keys = {
            'consumer_key':        lines[1].strip(),
            'consumer_secret':     lines[3].strip(),
            'bearer_token':        lines[5].strip(),
            'access_token_key':    lines[7].strip(),
            'access_token_secret': lines[9].strip(),
            'client_key':          lines[11].strip(),
            'client_token':        lines[13].strip()
        }

    """Construct the authenticator"""
    auth = tweepy.OAuthHandler(twitter_keys['consumer_key'],
                               twitter_keys['consumer_secret'])

    """Set the access token from vars"""
    auth.set_access_token(twitter_keys['access_token_key'],
                          twitter_keys['access_token_secret'])

    """Construct the API object"""
    api = tweepy.API(auth)

    return api
