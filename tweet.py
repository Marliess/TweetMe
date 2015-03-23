'''
Authors:
Gijs Hendriks - s2410540
Sil de Graaf -
Marlies Quekel - s2440571

Supervisor:
GJ van Noord
'''
import word

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
        words = text.split(' ')
        ''' Removes empty entrys when tweets end with a space'''
        words = [x for x in words if x]
        self.ryhmeWord = word.word(words[len(words)-1])
        
    def ryhmes(self, tweet):
        c1 = self.ryhmeWord.content
        c2 = tweet.ryhmeWord.content
        #First we determine how many letters we need to compare:
        #the last sequence of vowels and consonants
        compareLength  = self.getCompareLength(c1[5])
        r1 = self.ryhmeWord.phonetic
        r2 = tweet.ryhmeWord.phonetic
        print(r1)
        print(r2)
        
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
        return "Tweet-object:\nText: '" + self.text + "'\nLength " + str(self.length) + "\nRyhmeWord: '" + str(self.ryhmeWord) + "'"


print(tweet("blah blakd dlakj aardbeving  ").ryhmes(tweet("omgeving")))

