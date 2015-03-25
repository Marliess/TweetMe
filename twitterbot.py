#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Authors:
Gijs Hendriks	- s2410540
Sil de Graaf	- s2615703
Marlies Quekel	- s2440571

Supervisor:
GJ van Noord

twitteraccount: https://twitter.com/Twiettwiets

Aanroep: python twitterbot.py [bestand met rijmende tweets]
'''
 
import tweepy, time, sys, crawler

#argfile = str(sys.argv[1])
 

CONSUMER_KEY = 'UchYJE48vsV4goRWJMno3Frjw'
CONSUMER_SECRET = 'rGZimiUJNv3kCH6mHIkUUfeCi9DtdYTORLnTprpGF1W11KEcZG'
ACCESS_KEY = '3104614629-R5pGLEkV5UtlNf9PXGQ34XF8OVUsCNKdLSa5TO1'
ACCESS_SECRET = 'RiuNzKOU4oPkaxP2TAjlGPNlxuKnLWLMXEDvcFrFJOb5I'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

c = crawler.crawler()
while 1:
    tweets = c.ttGenerator()
    print(tweets)
    t1 = ' '.join(tweets[0])
    t2 = ' '.join(tweets[1])
    if len(t1) <= 128 and len(t2) <= 128:
        t1 = t1 + ' #Twiettwiet'
        t2 = t2 + ' #Twiettwiet'
        api.update_status(status=t1)
        time.sleep(1)
        api.update_status(status=t2)
        time.sleep(60) # Tweet elke minuut
    
"""print nu alleen nog de eerste line per status, dit moeten twee per keer worden!"""

"""used this tutorial: http://www.dototot.com/how-to-write-a-twitter-bot-with-python-and-tweepy/"""
