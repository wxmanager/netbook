import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5 import QtCore, QtGui
from uis.Ui_MainWindow import Ui_MainWindow
import os


class MainWindow:
    def __init__(self) -> None:
        self.mainwin = QMainWindow()
        self.uelement = Ui_MainWindow()

        self.uelement.setupUi(self.mainwin)
        self.mainwin.showFullScreen()

        self.uelement.exitButton.clicked.connect(sys.exit)

    def show(self):
        self.mainwin.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())