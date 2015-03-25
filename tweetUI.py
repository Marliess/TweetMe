'''
Authors:
Gijs Hendriks - s2410540
Sil de Graaf -
Marlies Quekel - s2440571

Supervisor:
GJ van Noord
'''

import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import random
import crawler

class tweetUI(QtGui.QWidget):
    def __init__(self, tweet, ryhmeTweet):
        """
        Constructor
        """
        super(tweetUI, self).__init__()
        self.tweet = tweet
        self.ryhmeTweet = ryhmeTweet
        self.initUI()

    def initUI(self):
        """
        Create labels and buttons to work with
        """
        self.grid = QtGui.QGridLayout()
        self.palette = QtGui.QPalette()
        self.tweetLabel = QtGui.QLabel()
        self.twietwietLabel = QtGui.QLabel()
        self.twietwietButton = QtGui.QPushButton('Nieuwe twietwiet', self)
        """
        Show background image
        Source: http://stackoverflow.com/questions/26217977/pyqt4-py3-cant-display-image-in-qframe-background
        """
        self.palette.setBrush(QtGui.QPalette.Background,QBrush(QPixmap("tweetMe.jpg")))
        self.setFixedSize(800,470)       
        self.setPalette(self.palette)
        """
        Set style and alignment of the text
        Source: http://pyqt.sourceforge.net/Docs/PyQt4/qapplication.html for setStylesheet
        Source: http://pyqt.sourceforge.net/Docs/PyQt4/qt-alignment.html for Alignment
        """
        self.tweetLabel.setStyleSheet('font-size: 12pt; font-family: Arial;')
        self.twietwietLabel.setStyleSheet('font-size: 12pt; font-family: Arial;')
        self.tweetLabel.setAlignment(Qt.AlignRight)
        self.twietwietLabel.setAlignment(Qt.AlignRight)
        """
        Set button size
        """
        self.twietwietButton.setFixedWidth(150)
        self.twietwietButton.move(320,50)
        self.tweetLabel.move(320,100)
        """
        Connect to event handler
        """
        self.twietwietButton.clicked.connect(self.eventHandler)
        """
        Add widget to variabel position
        """
        self.grid.addWidget(self.twietwietButton, 9,0)
        self.grid.addWidget(self.tweetLabel, 7,0)
        self.grid.addWidget(self.twietwietLabel, 8, 0)
        """
        Create window name, set geometry and show the screen
        """
        self.setWindowTitle("TwieTwiet Generator")
        self.setGeometry(500, 200, 600, 600)
        self.setLayout(self.grid)
        self.show()

    def eventHandler(self):
        """
        Event handler where a new tweet or twietwiet will be selected and displayed
        """
        source = self.sender()
        self.tweetLabel.clear()
        self.twietwietLabel.clear()
        """
        Convert tweet list to string, so it will be displayed nicely
        """
        str1 = ' '.join(self.tweet)
        str2 = ' '.join(self.ryhmeTweet)
        self.tweetLabel.setText(str1)
        self.twietwietLabel.setText(str2)


if __name__ == '__main__':
        app = QtGui.QApplication(sys.argv)
        twieTwiet = crawler.crawler()
        tweet = twieTwiet.twietwiet[0]
        ryhmeTweet = twieTwiet.twietwiet[1]
        widget = tweetUI(tweet,ryhmeTweet)
        widget.show()
        app.exec_()
