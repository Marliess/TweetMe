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
        self.twietwiet()                            # creates a twietwiet from usable tweetList


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
        allTweetList = [line.split() for line in open("tweets.txt", encoding="utf-8-sig")]
        self.tweetList = [tweet for tweet in allTweetList if tweet[-1] in self.prondict]
        return self.tweetList




    def twietwiet(self):
        tweetdict = {}
        self.twietwiet = []
        for tweet in self.tweetList:
            key = tweet[-1]
            value = self.prondict.get(key, 'unknown')
            tweetdict[key] = value
        while self.twietwiet == []:
            tweet1 = random.choice(self.tweetList)
            tweet2 = random.choice(self.tweetList)
            tweet1_value = tweetdict.get(tweet1[-1], 'unknown')
            tweet1_value = tweet1_value.strip("'")
            tweet2_value = tweetdict.get(tweet2[-1], 'unknown')
            tweet2_value = tweet2_value.strip("'")
            """len > 2, anders krijg je twietwiets waarbij ook op ik zou moeten rijmen omdat
            de value, dus de uitspraak vanaf het 2e teken is genomen"""
            if len(tweet2_value) > 2 and len(tweet1_value) > 2:
                if tweet2 != tweet1 and tweet2_value[1:] == tweet1_value[1:] and tweet2_value != tweet1_value:
                    self.twietwiet.append(tweet1)
                    self.twietwiet.append(tweet2)
                else:
                    tweet2 = random.choice(self.tweetList)
            else:
                tweet2 = random.choice(self.tweetList)
        
        print(self.twietwiet)
        return self.twietwiet


if __name__ == "__main__":
    crawler()

