# System functions
import sys
from datetime import datetime
import time
import os
import random

# Qt5
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5 import QtCore, QtGui
from uis.Ui_MainWindow import Ui_MainWindow
from PyQt5.QtCore import QTimer, QTime



welcomes = ["Welcome!", "Hello", "G'Day!", "Get to browsing!"]


class MainWindow:
    def __init__(self) -> None:
        self.mainwin = QMainWindow()
        self.uielement = Ui_MainWindow()

        self.uielement.setupUi(self.mainwin)
        self.mainwin.showFullScreen()

        self.uielement.exitButton.clicked.connect(sys.exit)
        self.uielement.welcomeLabel.setText("Hello world")
        self.clock = self.uielement.timeLabel

        self.timer = QTimer()
        self.timer.timeout.connect(self.gettime)
        self.timer.start(1000)
        

        

        


    def gettime(self):
        nowtime = datetime.now()
        clockvar = nowtime.strftime("%I:%M:%S %p - %D")
        self.clock.setText(clockvar)
        
         


    def show(self):
        self.mainwin.show()
        self.gettime()

    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())



