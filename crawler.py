'''
Authors:
Gijs Hendriks - s2410540
Sil de Graaf -
Marlies Quekel - s2440571

Supervisor:
GJ van Noord
'''

#import tweet
#import sys
import random

class crawler():
    '''
    A class to 'walk' through all the tweets and compare them and find their twietwiets
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.tweet = open("tweets.txt","r")         # opens a textfile with tweets
        self.prondict()                             # creates a pronunciation dictionary
        self.tweetList()                            # file that contains all usable tweets
        self.twietwiet()                            # creates a twietwiet from usable tweetList
        


    def prondict(self):
        pronlist = [line.split('\\') for line in open("dpw.cd")]
        self.prondict = {}
        for self.text in pronlist:
            key = self.text[1]
            value = self.text[3]
            self.prondict[key] = value
        return self.prondict



    def tweetList(self):
        self.tweetList = []
        allTweetList = [line.split() for line in open("tweets.txt")]
        for tweet in allTweetList:
            if tweet[-1] in self.prondict:
                self.tweetList.append(tweet)
        return self.tweetList



if __name__ == "__main__":
    crawler()

