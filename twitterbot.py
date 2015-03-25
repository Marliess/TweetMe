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
 
argfile = str(sys.argv[1])
 

CONSUMER_KEY = 'UchYJE48vsV4goRWJMno3Frjw'
CONSUMER_SECRET = 'rGZimiUJNv3kCH6mHIkUUfeCi9DtdYTORLnTprpGF1W11KEcZG'
ACCESS_KEY = '3104614629-R5pGLEkV5UtlNf9PXGQ34XF8OVUsCNKdLSa5TO1'
ACCESS_SECRET = 'RiuNzKOU4oPkaxP2TAjlGPNlxuKnLWLMXEDvcFrFJOb5I'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
 
filename=(argfile,'r')
f=filename.readlines()
filename.close()
 
for line in f:
    api.update_status(status=line)
    time.sleep(60) # Tweet elke minuut
    
"""print nu alleen nog de eerste line per status, dit moeten twee per keer worden!"""

"""used this tutorial: http://www.dototot.com/how-to-write-a-twitter-bot-with-python-and-tweepy/"""
