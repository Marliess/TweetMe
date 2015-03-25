'''
Authors:
Gijs Hendriks - s2410540
Sil de Graaf -
Marlies Quekel - s2440571

Supervisor:
GJ van Noord
'''

import random

class crawler():
    '''
    A class to 'walk' through all the tweets and compare them and find their twietwiets
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.prondict()                             # creates a pronunciation dictionary
        self.tweetList()                            # file that contains all usable tweets
        self.ttGenerator()                          # creates a twietwiet from usable tweetList

    def prondict(self):
        '''
        A dictionary with words and their phonetic pronunciation
        '''
        pronlist = [line.split('\\') for line in open("dpw.cd")]
        self.prondict = {}
        for self.text in pronlist:
            key = self.text[1]
            value = self.text[3]
            self.prondict[key] = value
        return self.prondict

    def tweetList(self):
        '''
        Create a tweetList with all the usable tweets
        '''
        allTweetList = [line.split() for line in open("tweets.txt")]
        self.tweetList = [tweet for tweet in allTweetList if tweet[-1] in self.prondict]
        return self.tweetList


    def ttGenerator(self):
        tweetdict = {}
        self.twietwiet = []
        '''
        A dictionary with the last words, the ryhming words, of tweets
        '''
        for tweet in self.tweetList:
            key = tweet[-1]
            value = self.prondict.get(key, 'unknown')
            tweetdict[key] = value
        '''
        While list is empthy pick a random tweet from the list and compare with another tweet for ryhming
        '''
        while self.twietwiet == []:
            tweet = random.choice(self.tweetList)
            ryhmeTweet = random.choice(self.tweetList)
            tweetValue = tweetdict.get(tweet[-1], 'unknown')
            tweetValue = tweetValue.strip("'")
            ryhmeTweetValue = tweetdict.get(ryhmeTweet[-1], 'unknown')
            ryhmeTweetValue = ryhmeTweetValue.strip("'")
            '''
            The words from tweet and ryhmetweet have to be bigger than 2, because with a word of 2 letters you can't make a good ryhme
            '''
            if len(ryhmeTweetValue) > 2 and len(tweetValue) > 2:
                if ryhmeTweet != tweet and ryhmeTweetValue[1:] == tweetValue[1:] and ryhmeTweetValue != tweetValue:
                    self.twietwiet.append(tweet)
                    self.twietwiet.append(ryhmeTweet)
                else:
                    ryhmeTweet = random.choice(self.tweetList)
            else:
                ryhmeTweet = random.choice(self.tweetList)

        print(self.twietwiet)
        return self.twietwiet


if __name__ == "__main__":
    crawler()

