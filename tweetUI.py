import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import random

class tweetUI(QtGui.QWidget):
    def __init__(self, tweet1, tweet2):
        """
        Constructor
        """
        super(tweetUI, self).__init__()
        self.tweet1 = tweet1
        self.tweet2 = tweet2
        self.initUI()

    def initUI(self):
        """
        Create labels and buttons to work with
        """
        self.grid = QtGui.QGridLayout()
        self.palette = QtGui.QPalette()
        self.tweetLabel = QtGui.QLabel()
        self.twietwietLabel = QtGui.QLabel()
        self.tweetButton = QtGui.QPushButton('Nieuwe tweet', self)
        self.twietwietButton = QtGui.QPushButton('Nieuwe twietwiet', self)
        """
        show a background image
        """
        self.palette.setBrush(QtGui.QPalette.Background,QBrush(QPixmap("tweetMe.jpg")))     #"twitter.png"
        self.setFixedSize(800,470)       # self.setFixedSize(738,415)
        self.setPalette(self.palette)
        """
        Set style and alignment of the text
        """
        self.tweetLabel.setStyleSheet('font-size: 25pt; font-family: Arial;')
        self.twietwietLabel.setStyleSheet('font-size: 25pt; font-family: Arial;')
        self.tweetLabel.setAlignment(Qt.AlignRight)
        self.twietwietLabel.setAlignment(Qt.AlignRight)
        """
        Set button size
        """
        self.tweetButton.setFixedWidth(150)
        self.twietwietButton.setFixedWidth(150)
        """
        Connect to event handler
        """
        self.tweetButton.clicked.connect(self.eventHandler)
        self.twietwietButton.clicked.connect(self.eventHandler)
        """
        Add widget to variabel position
        """
        self.grid.addWidget(self.tweetLabel, 1, 1)
        self.grid.addWidget(self.twietwietLabel, 2, 1)
        self.grid.addWidget(self.tweetButton, 1, 0)
        self.grid.addWidget(self.twietwietButton, 2, 0)
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
        if source.text() == "Nieuwe tweet":
            self.tweetLabel.setText(random.choice(self.tweet1))
        else:
            self.twietwietLabel.setText(random.choice(self.tweet2))


if __name__ == '__main__':
        tweet1 = ['lekker','random','woorden','neerzetten','test']
        tweet2 = ['testen','of','dit','werkt','haha']
        app = QtGui.QApplication(sys.argv)
        t = tweetUI(tweet1, tweet2)
        t.show()
        app.exec_()
