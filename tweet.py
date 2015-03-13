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
        self.ryhmeWord = word.word(words[len(words)-1])
        
    def ryhmes(self, tweet):
        if self.ryhmeWord.phonetic == tweet.ryhmeWord.phonetic:
            return 1
        else:
            return 0
    
    def __str__(self):
        return "Tweet-object:\nText: '" + self.text + "'\nLength " + str(self.length) + "\nRyhmeWord: '" + str(self.ryhmeWord) + "'"


t = tweet("@aafkevultink zal nog wel een aantal jaren duren voor nieuwe afspraken")
print(t)
