import datetime
import logging
import sys
import keyboard
import time
import mouse
import ctypes

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
        keyboard.on_press(self.KeyStrokeIncrement, False)
    
    def SetupMouseHook(self):
        mouse.hook(self.MouseIncrement)

    def MouseIncrement(self, event):
        # print(type(event))
        if isinstance(event, mouse.ButtonEvent):
            self.mouseClickCount += 1
        elif isinstance(event, mouse.WheelEvent):
            self.scrollCount += 1

    def KeyStrokeIncrement(self, x):
        self.keyCount += 1

    # def LowProductivityPrompt(self):
    #     result = ctypes.windll.user32.MessageBoxW(0, "Your Productivity is too low. Take a break?", "Low Productivity", 1)
    #     # 1 means OK, 2 means cancel
    #     if result is 1:
    #         sys.exit()

