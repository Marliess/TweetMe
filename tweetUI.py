'''
Authors:
Gijs Hendriks - s2410540
Sil de Graaf - s2615703
Marlies Quekel - s2440571

Supervisor:
GJ van Noord
'''

import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import random
import crawler as c

class tweetUI(QtGui.QWidget):
    def __init__(self):
        """
        Constructor
        """
        super(tweetUI, self).__init__()
        self.crawler = c.crawler()
        self.initUI()

    def initUI(self):
        """
        Create labels and buttons to work with
        """
        self.grid = QtGui.QGridLayout()
        self.palette = QtGui.QPalette()
        self.tweetLabel = QtGui.QLabel()
        self.tweetLabelRWord = QtGui.QLabel()
        self.twietwietLabel = QtGui.QLabel()
        self.twietwietLabelRWord = QtGui.QLabel()
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
        self.tweetLabelRWord.setStyleSheet('font-size: 20pt; font-family: Arial;')
        self.twietwietLabelRWord.setStyleSheet('font-size: 20pt; font-family: Arial;')
        """
        Connect to event handler
        """
        self.twietwietButton.clicked.connect(self.eventHandler)
        """
        Add widget to variabel position
        """
        self.grid.addWidget(self.tweetLabel, 0,0, QtCore.Qt.AlignCenter)
        self.grid.addWidget(self.tweetLabelRWord, 1,0, QtCore.Qt.AlignCenter)
        self.grid.addWidget(QtGui.QWidget(),2,0)
        self.grid.addWidget(QtGui.QWidget(),3,0)
        
        self.grid.addWidget(self.twietwietLabel, 4, 0, QtCore.Qt.AlignCenter)
        self.grid.addWidget(self.twietwietLabelRWord, 5, 0, QtCore.Qt.AlignCenter)
        self.grid.addWidget(QtGui.QWidget(),6,0)
        self.grid.addWidget(QtGui.QWidget(),7,0)       
        self.grid.addWidget(self.twietwietButton, 8,0)
        """
        Create window name, set geometry and show the screen
        """
        self.setWindowTitle("TwieTwiet Generator")
        self.setGeometry(500, 200, 500, 500)
        self.setLayout(self.grid)
        self.show()

    def eventHandler(self):
        """
        Event handler where a new tweet or twietwiet will be selected and displayed
        """
        source = self.sender()
        tweets = self.crawler.ttGenerator()
        self.tweetLabel.setText(' '.join(tweets[0]))
        self.tweetLabelRWord.setText(tweets[0][-1])
        self.twietwietLabel.setText(' '.join(tweets[1]))
        self.twietwietLabelRWord.setText(tweets[1][-1])

if __name__ == '__main__':
        app = QtGui.QApplication(sys.argv)
        widget = tweetUI()
        widget.show()
        app.exec_()
