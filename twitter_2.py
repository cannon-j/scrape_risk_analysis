import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import argparse
import string
import config
import json

#query = ['Asset bubble','equity bubble','subprime','investment bubble','deflation','falling inflation','reduced inflation','falling prices','energy price','gasoline price','petrol price','bank failure','bank collapse','market collapse','market failure','bank bailout','critical infrastructure','infrastructure failure','fiscal crisis','financial crisis','underemployment','unemployment','Inflation','Storm','Flood','Extreme weather','Climate change','biodiversity','natural disaster','oil spill','environmental contamination','corruption','organized crime','war','state conflict','terrorism','terrorist','state collapse','civil crisis','coup','failed state','WMD','nuclear weapon','nuke','dirty bomb','failed urban planning','food crisis','starvation','refugee','refugees','riot','infectious','disease','epidemic','pandemic','drought','water shortage','internet collapse','cyber attack','cyber warfare','cyber terrorism','data fraud','identity theft','misuse of technology']

data_file = 'data.txt'

class MyListener(StreamListener):
    """Custom StreamListener for streaming data."""

    def __init__(self, data_file, query):
        self.outfile = data_file

    def on_data(self, data):
        try:
            with open(self.outfile, 'a') as f:
                parsed_json = json.loads(str(data))
                f.write(parsed_json['text'].encode('utf-8'))
                print(parsed_json['text'].encode('utf-8'))
                return True
            
        except BaseException as e:
            print("Error on_data: %s" % str(e))
            time.sleep(5)
            
        return True
    
if __name__ == '__main__':
    auth = OAuthHandler(config.consumer_key, config.consumer_secret)
    auth.set_access_token(config.access_token, config.access_secret)
    api = tweepy.API(auth)

    twitter_stream = Stream(auth, MyListener(data_file, query))
    twitter_stream.filter(track=query)