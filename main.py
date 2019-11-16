from OptimusTime import OptimusTime
import sys
import logging
import datetime
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

# This is the entry-point for the application.
if __name__ == '__main__':
    # Instantiate the time optimizer
    optimusTime = OptimusTime()
    # optimusTime.LowProductivityPrompt()

    # Form, Window = uic.loadUiType("C:\Users\Lexy\Documents\PycharmProjects\PersonalProjects\OptimusTime"
    #                               "\Low Productivity Prompt.ui")
    #
    # app = QApplication([])
    # window = Window()
    # form = Form()
    # form.setupUi(window)
    # window.show()
    # app.exec_()