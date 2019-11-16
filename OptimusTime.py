import datetime
import logging
import sys
import os
import threading
import random
import time
from pynput import mouse
from pynput import keyboard
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class OptimusTime(QWidget):
    def __init__(self):
        super().__init__()
        # initialize logging
        if os.path.isdir(os.getcwd()+"/logs") == False:
            os.mkdir(os.getcwd()+"/logs")
        logging.basicConfig(filename=sys.path[0]+'/logs/'+str(datetime.date.today())+'.log', level=logging.INFO,format=str(datetime.datetime.now())+' %(levelname)s:  %(message)s')
        self.keyCount = 0
        self.mouseClickCount = 0
        self.scrollCount = 0
        self.startedAt = datetime.datetime.now()
        self.SetupKeyboardHook()
        time.sleep(1)
        self.SetupMouseHook()
        self.timer = threading.Timer(2*1, self.timerInterval)
        self.title = 'Optimus Time'
        self.left = 10
        self.top = 10
        self.width = 250
        self.height = 75
        self.maximumHeight = 75
        self.minimumHeight = 75
        self.maximumWidth = 250
        self.minimumWidth = 250
        self.timerEnabled = False
        self.initUI()
    
    def initUI(self):
        startButton = QPushButton('Start', self)
        startButton.setToolTip('Start tracking your effectivness')
        startButton.move(10,40)
        startButton.setMinimumWidth(120)
        startButton.height = 32
        startButton.clicked.connect(self.Start)

        stopButton = QPushButton('Stop', self)
        stopButton.setToolTip('Stop tracking your effectivness')
        stopButton.move(125,40)
        stopButton.setMinimumWidth(120)
        stopButton.height = 32
        stopButton.clicked.connect(self.Stop)
        
        self.apmLabel = QLabel('0', self)
        self.apmLabel.width = 91
        self.apmLabel.height = 31
        self.apmLabel.move(155,8)
        self.apmLabel.setFont(QFont('Arial', 24))
        self.apmLabel.setAlignment(Qt.AlignRight)

        infoLabel = QLabel('Actions Per Minute', self)
        infoLabel.width = 151
        infoLabel.height = 51
        infoLabel.setFont(QFont('Arial', 12))
        infoLabel.move(15,15)
        
        self.show()

    def GetActionCount(self):
        return self.keyCount + self.mouseClickCount + self.scrollCount

    def resetActionCounts(self):
        self.keyCount = 0
        self.mouseClickCount = 0
        self.scrollCount = 0
    
    def Start(self):
        # start button clicked
        self.timerEnabled = True
        self.timer.start()
        print('Started')
    
    def Stop(self):
        # start button clicked
        self.timerEnabled = False
        self.timer.cancel()
        print('Stopped')

    def SetupKeyboardHook(self):
        listener = keyboard.Listener(
            on_release=self.on_release)
        listener.start()
    
    def on_click(self, x, y, button, pressed):
        if not pressed:
            self.mouseClickCount += 1

    def on_scroll(self, x, y, dx, dy):
            self.scrollCount += 1

    def on_release(self, key):
        self.keyCount += 1

    def SetupMouseHook(self):
        listener = mouse.Listener(
            on_click=self.on_click,
            on_scroll=self.on_scroll)
        listener.start()

    def LowProductivityPrompt(self):
        print("low prodcutivity trigger")
        Dialog, DialogWindow = uic.loadUiType("Low Productivy Prompt.ui")
        dialogWindow = DialogWindow()
        dialog = Dialog()
        dialog.setupUi(dialogWindow)
        dialogWindow.exec()

    def timerInterval(self):
        if self.timerEnabled:
            #if self.GetActionCount() < 10:
            #self.LowProductivityPrompt()  
            self.apmLabel.setText(str(self.GetActionCount()))
            self.resetActionCounts()
            time.sleep(2)
            print("Timer reset")
            self.timerInterval()
