'''
Authors:
Gijs Hendriks - s2410540
Sil de Graaf -
Marlies Quekel - s2440571

Supervisor:
GJ van Noord
'''

import random
import tweet as t
import string

class crawler():
    '''
    A class to 'walk' through all the tweets and compare them and find their twietwiets
    '''

    def __init__(self):
        #pronunciation dictionary
        self.pd = {}
        self.tweets = []
        for line in open("dpw.cd"):
            l = line.split('\\')
            #print(l[1], l[4],l[5])
            self.pd[l[1]] = (l[4], l[5])
        lines = [line for line in open('tweets.txt', encoding='utf-8-sig')]
        for line in lines:
            words = ''.join(c for c in line if c not in string.punctuation)
            words = words.rstrip().split(' ')
            if words[-1] in self.pd:
                self.tweets.append(t.tweet(line, self.pd[words[-1]]))
        print(self.tweets)
    def randomCouple(self):
        pass

    def giveNext(self, tweet):
        pass

crawler()
