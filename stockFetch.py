import tweepy 
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('API_KEY')
api_secret = os.getenv('API_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')
bearer_token = os.getenv('BEARER_TOKEN')

client = tweepy.Client(bearer_token, api_key,api_secret, access_token, access_token_secret)

def tweet(params):
    tweetVal = ""
    for stock in params:
        tweetVal += stock + "\n"
        
    client.create_tweet(text=tweetVal, user_auth=True)
    print("tweet Successful!")