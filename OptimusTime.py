import datetime
import logging
import sys
import os
import threading
from pynput import mouse
from pynput import keyboard
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import *

class OptimusTime:
    def __init__(self):
        # initialize logging
        if os.path.isdir(os.getcwd()+"/logs") == False:
            os.mkdir(os.getcwd()+"/logs")
        logging.basicConfig(filename=sys.path[0]+'/logs/'+str(datetime.date.today())+'.log', level=logging.INFO,format=str(datetime.datetime.now())+' %(levelname)s:  %(message)s')
        self.keyCount = 0
        self.mouseClickCount = 0
        self.scrollCount = 0
        self.startedAt = datetime.datetime.now()
        self.SetupKeyboardHook()
        self.SetupMouseHook()
        self.timer = threading.Timer(5, self.timerInterval)

    def GetActionCount(self):
        return self.keyCount + self.mouseClickCount + self.scrollCount

    def resetActionCounts(self):
        self.keyCount = 0
        self.mouseClickCount = 0
        self.scrollCount = 0
    
    def Start(self):
        # start button clicked
        self.timer.start()
        print('Started')
    
    def Stop(self):
        # start button clicked
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
        print("low prodcutivity tirgger")
        Dialog, DialogWindow = uic.loadUiType("Low Productivy Prompt.ui")
        dialogWindow = DialogWindow()
        dialog = Dialog()
        dialog.setupUi(dialogWindow)
        dialogWindow.show()
        exit()

    def timerInterval(self):
        if self.GetActionCount() < 30:
            self.LowProductivityPrompt()
        self.resetActionCounts()
        self.timer.start()
        print("Timer reset")
