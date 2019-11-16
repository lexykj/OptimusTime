import sys
import logging
import datetime
<<<<<<< Updated upstream
from MainForm import MainForm
=======
from OptimusTime import OptimusTime
from PyQt5 import uic
>>>>>>> Stashed changes
from PyQt5.QtWidgets import QApplication

# This is the entry-point for the application.
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = OptimusTime()
    sys.exit(app.exec_())
