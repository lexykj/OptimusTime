from OptimusTime import OptimusTime
import sys
import logging
import datetime
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

# This is the entry-point for the application.
if __name__ == '__main__':

    Dialog, DialogWindow = uic.loadUiType("Low Productivy Prompt.ui")
    app = QApplication([])
    dialogWindow = DialogWindow()
    dialog = Dialog()
    dialog.setupUi(dialogWindow)
    dialogWindow.show()
    app.exec_()
    exit()
    # Instantiate the time optimizer
    #optimusTime = OptimusTime()
    
