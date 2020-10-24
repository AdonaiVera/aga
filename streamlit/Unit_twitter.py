import re
import tweepy
import time
from sqlalchemy import create_engine, text
from textblob import TextBlob
import pandas as pd
from listener_twitter import TwStreamListener


print("Start process")
myStreamListener = TwStreamListener()
myStreamListener.connect()
# Write the topics that you are interesting.

# Agregar un selector de estas variables.

TRACK_WORDS = ['seguridad']

# The location is a rectangle whose first two coordinates (longitude and latitude) are the bottom left corner and the last two are the top right corner.
# We use https://boundingbox.klokantech.com/ to get the bounding box of the place that we wanna know.

LOCATION_BELLO = [-75.623604,6.303511,-75.493611,6.373763]



myStreamListener.run(TRACK_WORDS, LOCATION_BELLO)

# Check my database
sql = """SELECT * FROM twitter LIMIT 10;"""
final = myStreamListener.runQuery(sql)

print("Stop process")
final.head(5)
