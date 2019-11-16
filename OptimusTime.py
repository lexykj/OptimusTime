import datetime
import logging
import sys
import os
import time
from pynput import mouse
from pynput import keyboard
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

    def GetActionCount(self):
        return self.keyCount + self.mouseClickCount + self.scrollCount
    
    def Start(self):
        # start button clicked
        print('Started')
    
    def Stop(self):
        # start button clicked
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
        Dialog, DialogWindow = uic.loadUiType("Low Productivy Prompt.ui")
        app = QApplication([])
        dialogWindow = DialogWindow()
        dialog = Dialog()
        dialog.setupUi(dialogWindow)
        dialogWindow.show()
        app.exec_()
        exit()
