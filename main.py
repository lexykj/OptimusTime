import sys
import logging
import datetime
from OptimusTime import OptimusTime
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

# This is the entry-point for the application.
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = OptimusTime()
    sys.exit(app.exec_())
