import machine
from machine import Pin
from stm import pulsefeedback_read
from BrainPadUtil import *

class Touch:
    def __init__(self, pin, sensitiveLevel):
        self.pin =  Pin(GetPinFromString(pin))
        self.sensitive = 100 - sensitiveLevel
        
    def In(self):
        t = pulsefeedback_read(self.pin)
        scale =  Scale(t, 8, 14, 0, 100)
        
        if (scale >= self.sensitive):
            return 1
        else:
            return 0
        

        
        
        
        
        
        