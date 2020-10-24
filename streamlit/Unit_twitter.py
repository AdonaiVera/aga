import re
import tweepy
import time
from sqlalchemy import create_engine, text
from textblob import TextBlob
import pandas as pd
from listener_twitter import TwStreamListener



myStreamListener = TwStreamListener()
myStreamListener.connect()
TRACK_WORDS = ['seguridad']
LOCATION_BELLO = [-75.623604,6.303511,-75.493611,6.373763]
myStreamListener.run(TRACK_WORDS, LOCATION_BELLO)


