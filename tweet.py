'''
Authors:
Gijs Hendriks - s2410540
Sil de Graaf -
Marlies Quekel - s2440571
Supervisor:
GJ van Noord
'''

import string

class tweet():
    '''
    A class to represent a tweet
    '''

    def __init__(self, text, phonetic):
        '''
        Initializes the tweet
        '''
        self.text = text
        #self.user = user
        #self.date = date
        #self.length = len(text)

        
        #''' Removes puctuation '''
        #words = ''.join(c for c in self.text if c not in string.punctuation)
        #''' Removes empty entrys when tweets end with a space and/or newline'''
        #words = words.rstrip().split(' ')
        self.phonetic = phonetic


        
    def ryhmes(self, tweet):
        if (self.phonetic == tweet.phonetic):
            return 0

        
        #First we determine how many letters we need to compare:
        #the last sequence of vowels and consonants
        compareLength  = self.getCompareLength(self.phonetic[1])
        r1 = self.phonetic[0]
        r2 = tweet.phonetic[0]
        
        for x in range(1, compareLength+1):
            #print (x, r1[len(r1) - x], r2[len(r2) - x])
            if r1[len(r1) - x] != r2[len(r2) - x]:
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
            elif c == "C":
                i += 1
        
        #print(string[-i:])
        
        return i
    
    def __str__(self):
        return "Tweet-object:\nText: '" + self.text + "\nRyhmeWord: '" + str(self.phonetic) + "'"


#t = tweet('ksksl aanminnigst',('[a:n][mI[n]@xst]', '[VVC][CV[C]VCCC]\n'))
#print(t)
#print(t.getCompareLength('[VVC][CV[C]VCCC]'))
#print(t.ryhmes(tweet('minnigstdafdsfd', ('[n][mI[n]@xst]', '[VVC][CV[C]VCCC]\n'))))
