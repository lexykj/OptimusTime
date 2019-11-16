import datetime
import logging
import sys
import keyboard
import time
import mouse

class OptimusTime:
    def __init__(self):
        # initialize logging
        logging.basicConfig(filename=sys.path[0]+'/logs/'+str(datetime.date.today())+'.log', level=logging.INFO,format=str(datetime.datetime.now())+' %(levelname)s:  %(message)s')
        self.keyCount = 0
        self.mouseClickCount = 0
        self.scrollCount = 0
        self.startedAt = datetime.datetime.now()
        # self.SetupKeyboardHook()
        self.SetupMouseHook()
    
    def SetupKeyboardHook(self):
        time.sleep(5)
        keyboard.write('TESTTESTTEST.')
    
    def SetupMouseHook(self):
        mouse.on_click(self.mouseTest)

    def mouseTest(self):
        print("click")
