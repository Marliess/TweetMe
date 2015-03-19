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
        self.ryhmeWord = word.word(words[len(words)-1])     # RyhmeWord is 'afspraken'
        tweet.ryhmeWord = word.word(words[len(words) -1])   # klopt nog niet, is nu ook 'afspraken'
        self.ryhmes(tweet)
        
    def ryhmes(self, tweet):
        if self.ryhmeWord.phonetic == tweet.ryhmeWord.phonetic:
            print("{} == {} so this ryhmes").format(self.ryhmeWord.phonetic, tweet.ryhmeWord.phonetic)
            return 1
        else:
            print("This doesn't ryhme")
            return 0
    
    def __str__(self):
        return "Tweet-object:\nText: '" + self.text + "'\nLength " + str(self.length) + "\nRyhmeWord: '" + str(self.ryhmeWord) + "'"


t = tweet("@aafkevultink zal nog wel een aantal jaren duren voor nieuwe afspraken")
print(t)
