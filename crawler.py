'''
Authors:
Gijs Hendriks - s2410540
Sil de Graaf -
Marlies Quekel - s2440571

Supervisor:
GJ van Noord
'''

import tweet
import sys

class crawler():
    '''
    A class to 'walk' through all the tweets and compare them
    '''

    def __init__(self,argv):
        '''
        Makes an list of all tweets and initializes an list for tweed tweets
        '''
        self.tweet = argv[1]
        self.listTweets()
        pass

    def listTweets(self):
        '''
        returns a list of all tweets
        '''
        tweets = []
        for line in open(self.tweet):
            tweets.append(line)
        tweetList = "\n".join(tweets)
        return tweetList
        pass

    def randomCouple(self):
        '''
        returns a tuple of two random ryhming tweets
        '''
        pass

    def giveNext(self, tweet):
        '''
        returns a tweet that ryhmes with given tweet and that is also not been returned yet
        '''
        pass

tweetMe = crawler(sys.argv)

