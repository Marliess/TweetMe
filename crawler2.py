'''
Authors:
Gijs Hendriks - s2410540
Sil de Graaf -
Marlies Quekel - s2440571

Supervisor:
GJ van Noord
'''

import random as r
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
            words = [x for x in words if x]
            if words[-1] in self.pd:
                self.tweets.append(t.tweet(line, self.pd[words[-1]]))
                
    def randomCouple(self):
        while 1:
            t1 = r.choice(self.tweets)
            t2 = r.choice(self.tweets)
            if t1.ryhmes(t2):
                print(t1, t2)
                break
        

    def giveNext(self, tweet):
        pass

crawler().randomCouple()
