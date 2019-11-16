import datetime
import logging
import sys
import time
from pynput import mouse
from pynput import keyboard
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

class OptimusTime:
    def __init__(self):
        # initialize logging
        logging.basicConfig(filename=sys.path[0]+'/logs/'+str(datetime.date.today())+'.log', level=logging.INFO,format=str(datetime.datetime.now())+' %(levelname)s:  %(message)s')
        self.keyCount = 0
        self.mouseClickCount = 0
        self.scrollCount = 0
        self.startedAt = datetime.datetime.now()
        self.SetupKeyboardHook()
        self.SetupMouseHook()
    
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
