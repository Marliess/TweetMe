# Documentatie Twiettwiets:
Authors:
Gijs Hendriks 		- s2410540
Sil de Graaf 		- s2615703
Marlies Quekel	- s2440571

Supervisor: 
GJ van Noord

## Introduction

Welcome by TweetMe. 
This is a program to create rhyming tweets, twietwiets, from a corpus of tweets.
These tweets will be displayed in a graphical user interface. You can click to a new twietwiet with a button called "New twietwiet".

## Handleiding

The program starts with a graphical user interface. When the user clicks on the Twietwiet button there will be a twietwiet displayed. The user can do an almost infinite amount of clicks before the twietwiets run out.

'Behind the scenes', there is a big tweet corpus, with all the tweets from 5 years in a row. This program picks a tweets and links it to a rhyming tweet. This compilation of rhyming tweets is called a twietwiet.
To see if tweets rhyme, the last word of a tweet will be compared to a 'rhyme dictionary', with their phonological representation. Matching these phonological representations gives you a twietwiet. And in the graphical user interface is where the user sees the twietwiet.

We also made a TwitterBot. This is a program to automatically tweet a twietwiet every minute. If you want to follow this account, go to www.twitter.com/twiettwiets

### Short summary of our programs
crawler.py
crawler.py exists of a class to 'walk' through all the tweets and compare them with a pronunciation dictionary and find their twietwiets. The crawler contains the pronunciation dictionary, a list with usable tweets and all rhymewords (the last word in every tweet).

dpw.cd
dpw.cd is our 'rhyme dictionary'. Words and their pronunciation are represented in this dictionary. 
By comparing words in the dictionary we know if they rhyme or not.

tweetMe.jpg
Contains the background image of the graphical user interface.

tweetUI.py
In this file we represent a class that 'shows' the actual graphical user interface to user. 
In TweetUI.py, InitUI(self) and eventHandler(self) are used.

tweet_corpora.txt
Our largest .txt file which contains millions of tweets (15 hours of tweets). 
We use this file to search for tweets that rhyme.

tweets.txt
Tweet corpus which contains tweets from 1 hour on 1 day.  
We use this file to test for tweets that rhyme.

twitterbot.py
This program automatically tweets twietwiets on our Twitter account (twitter.com/Twiettwiets).
It also puts a #Twietwiet at the end of the tweet.
