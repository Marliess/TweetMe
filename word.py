'''Authors:
Gijs Hendriks - s2410540
Sil de Graaf -
Marlies Quekel - s2440571

Supervisor:
GJ van Noord'''


class word():
    '''
    A class to represent a word and its phonetic pronunciation.
    '''
    
    def __init__(self, text):
        self.text = text
        self.valid = 0
        ''' Write file to array '''
        lines = [line.split('\\') for line in open("dpw.cd")]
        ''' Walk trough file to find the right word '''
        for line in lines:
            if self.text == line[1]:
                self.index = int(line[0])-1
                self.phonetic = line[4]
                self.valid = 1
                self.content = line
        ''' Check if word is found '''
        if(self.valid):
            #print (lines[self.index])
            pass
        else:
            print('Error: word not found inside dpw.cd: {}'.format(self.text))

    def __str__(self):
        
        return str(self.text)
        

#word('trottoir')
#word('kunstenaar')
#word('klaar')
#word('reservoir')
