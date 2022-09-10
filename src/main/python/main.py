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
from PyQt5.QtCore import *

# QT WebEngine Widgets
from PyQt5.QtWebEngineWidgets import *


welcomes = ["Hi!", "Hey there!", "How are things?", "It’s good to see you", "G’day!", "Howdy!", "What’s up?", "How’s it going?", "What’s happening?"]



class MainWindow:
    def __init__(self) -> None:
        self.mainwin = QMainWindow()
        self.uielement = Ui_MainWindow()

        self.uielement.setupUi(self.mainwin)
        self.mainwin.showFullScreen()

        self.uielement.exitButton.clicked.connect(sys.exit)
        self.clock = self.uielement.timeLabel

        self.timer = QTimer()
        self.timer.timeout.connect(self.gettime)
        self.timer.start(1000)

        self.uielement.openButton.clicked.connect(self.load_file)
        self.uielement.saveButton.clicked.connect(self.save_file)

        self.uielement.plainTextEdit.setPlaceholderText("Hey... You can write something here ;)")
        self.url = ''
        self.WebEngine = QWebEngineView()
        self.uielement.webLayout.addWidget(self.WebEngine)

        self.uielement.urlBar.returnPressed.connect(self.navigate_to_url)
        
        self.uielement.backButton.clicked.connect(self.WebEngine.back)
        self.uielement.forwardButton.clicked.connect(self.WebEngine.forward)
        self.uielement.reloadButton.clicked.connect(self.WebEngine.reload)

        self.uielement.cmdinput.returnPressed.connect(self.runCommand)

    
    def runCommand(self):
                command_line = self.uielement.cmdinput.text()
                p = os.popen(command_line)
                if p:
                    self.uielement.cmdinput.clear()
                    output = p.read()
                    self.uielement.cmdoutput.insertPlainText(output)
        
        
    
    def randomwelcome(self):
        self.uielement.welcomeLabel.setText(random.choice(welcomes))

    def gettime(self):
        nowtime = datetime.now()
        clockvar = nowtime.strftime("%I:%M:%S %p - %D")
        self.clock.setText(clockvar)
    
    def load_file(self):
        load_dlg = QFileDialog()
        f_name = load_dlg.getOpenFileName(load_dlg, caption="Load File")
        if not f_name[0] == "":
            with open(f_name[0], "r") as f:
                text = f.read()
                self.uielement.plainTextEdit.setPlainText(text)
                    

    def save_file(self):
        save_dlg = QFileDialog()
        f_name = save_dlg.getSaveFileName(save_dlg, caption="Save File")
        if not f_name[0] == "":
            with open(f_name[0], "w") as f:
                f.write(self.uielement.plainTextEdit.toPlainText())


        
    def navigate_to_url(self):
        q = QUrl(self.uielement.urlBar.text())
        self.WebEngine.setUrl(q)

    def show(self):
        self.mainwin.show()
        self.gettime()
        self.randomwelcome()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())



