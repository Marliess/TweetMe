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
    A class to 'walk' through all the tweets and compare them with a pronunciation dictionary and find their twietwiets
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
        allTweetList = [line.split() for line in open("tweet_corpora.txt")]
        self.tweetList = [self.tweet for self.tweet in allTweetList if self.tweet[-1] in self.prondict]
        return self.tweetList


    def ttGenerator(self):
        worddict = {}
        twietwiet = []
        '''
        A dictionary with the last words, the ryhming words, of tweets
        Source: http://stackoverflow.com/questions/8023306/get-key-by-value-in-dictionary for proper dictionary values
        '''
        for tweet in self.tweetList:
            lastword = tweet[-1]
            pron = self.prondict.get(lastword)
            worddict[lastword] = pron
        '''
        While list is empthy pick a random tweet from the list and compare with another tweet for ryhming
        '''
        while twietwiet == []:
            tweet = random.choice(self.tweetList)
            ryhmeTweet = random.choice(self.tweetList)
            
            tweetWord = worddict.get(tweet[-1])
            ryhmeTweetWord = worddict.get(ryhmeTweet[-1])
            tweetWord = tweetWord.strip("'")
            ryhmeTweetWord = ryhmeTweetWord.strip("'")
            '''
            The words from tweet and ryhmetweet have to be bigger than 2, because with a word of 2 letters you can't make a proper ryhme
            '''
            if len(tweetWord) > 2 and len(ryhmeTweetWord) > 2:
                if ryhmeTweetWord[1:] == tweetWord[1:] and ryhmeTweetWord != tweetWord:
                    twietwiet.append(tweet)
                    twietwiet.append(ryhmeTweet)
                else:
                    ryhmeTweet = random.choice(self.tweetList)
            else:
                ryhmeTweet = random.choice(self.tweetList)

        print(twietwiet)
        return twietwiet


if __name__ == "__main__":
    crawler()

