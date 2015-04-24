#Script created by @dattaniharsh, replace XXXX with your consumer_key, consumer_secret, access_token, access_token_secret after creating an application on twitter at apps.twitter.com

import tweepy
 
class TwitterAPI:
    def __init__(self):
        consumer_key = "XXXX"
        consumer_secret = "XXXX"
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        access_token = "XXXX"
        access_token_secret = "XXXX"
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)
 
    def tweet(self, message):
        self.api.update_status(status=message)
 
if __name__ == "__main__":
    twitter = TwitterAPI()
    twitter.tweet("Jay Bavarva!")
