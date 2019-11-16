import sys
from OptimusTime import OptimusTime
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Optimus Time'
        self.left = 10
        self.top = 10
        self.width = 250
        self.height = 75
        self.optimusTime = OptimusTime()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        startButton = QPushButton('Start', self)
        startButton.setToolTip('Start tracking your effectivness')
        startButton.move(10,40)
        startButton.setMinimumWidth(120)
        startButton.height = 32
        startButton.clicked.connect(self.start_button_on_click)

        stopButton = QPushButton('Stop', self)
        stopButton.setToolTip('Stop tracking your effectivness')
        stopButton.move(125,40)
        stopButton.setMinimumWidth(120)
        stopButton.height = 32
        stopButton.clicked.connect(self.stop_button_on_click)
        
        apmLabel = QLabel('0', self)
        apmLabel.width = 91
        apmLabel.height = 31
        apmLabel.move(155,8)
        apmLabel.setFont(QFont('Arial', 32))
        apmLabel.setAlignment(Qt.AlignRight)

        infoLabel = QLabel('Actions Per Minute', self)
        infoLabel.width = 151
        infoLabel.height = 51
        infoLabel.setFont(QFont('Arial', 16))
        infoLabel.move(15,15)
        
        self.show()

    @pyqtSlot()
    def start_button_on_click(self):
        self.optimusTime.Start()

    @pyqtSlot()
    def stop_button_on_click(self):
        self.optimusTime.Stop()