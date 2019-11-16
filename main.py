import sys
import logging
import datetime
from MainForm import MainForm
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

# This is the entry-point for the application.
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainForm()
    sys.exit(app.exec_())
