'''
Authors:
Gijs Hendriks - s2410540
Sil de Graaf -
Marlies Quekel - s2440571
Supervisor:
GJ van Noord
'''
import word
import string

class tweet():
    '''
    A class to represent a tweet
    '''

    def __init__(self, text):
        '''
        Initializes the tweet
        '''
        self.text = text
        #self.user = user
        #self.date = date
        self.length = len(text)
        ''' Removes puctuation '''
        words = ''.join(c for c in self.text if c not in string.punctuation)
        ''' Removes empty entrys when tweets end with a space and/or newline'''
        words = words.rstrip().split(' ')
        self.ryhmeWord = word.word(words[len(words)-1])


        
    def ryhmes(self, tweet):
        if not self.ryhmeWord.valid or not tweet.ryhmeWord.valid:
            return 0
        c1 = self.ryhmeWord.content
        c2 = tweet.ryhmeWord.content
        #First we determine how many letters we need to compare:
        #the last sequence of vowels and consonants
        compareLength  = self.getCompareLength(c1[5])
        r1 = self.ryhmeWord.phonetic
        r2 = tweet.ryhmeWord.phonetic
        
        for x in range(0, compareLength+1):
            #print(x)
            #print (r1[len(r1)-1-x])
            #print (r2[len(r2)-1-x])
            if r1[len(r1)-1-x] != r2[len(r2)-1-x]:
                ryhme = 0
                return 0
        return 1

    
    def getCompareLength(self, string):
        string = string.split('][')
        string = string[len(string)-1]
        string = string.replace(']\n', '')
        i = 1
        vowelsHaveBeen = 0
        for c in reversed(string):
            if c == "V":
                i += 1
                vowelsHaveBeen = 1
            elif c == "C" and vowelsHaveBeen == 1:
                break
        
        #print(string[-i:])
        
        return i
    
    def __str__(self):
        return "Tweet-object:\nText: '" + self.text + "'\nLength: " + str(self.length) + "\nRyhmeWord: '" + str(self.ryhmeWord) + "'"


tweets = [line for line in open('tweets.txt')]
for t1 in tweets:
    for t2 in tweets:
        #print(tweet(t1))
        #print(tweet(t2))
        print(tweet(t1).ryhmes(tweet(t2)))

#print(tweet("blah blakd dlakj aardbeving   !! \n  ").ryhmes(tweet("omgeving")))
