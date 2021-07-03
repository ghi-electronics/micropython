import machine
from machine import Pin
import utime
import time
from BrainPadUtil import *

class Buttons:                    
    def __init__(self, pin, detectPeriod):
        self.pin = GetPinFromString(pin)
        self.period = detectPeriod * 1000
        self.WasPressed = False        
        self.Btn = Pin(self.pin,Pin.IN, Pin.PULL_UP)        
        self.Btn.irq(trigger=Pin.IRQ_FALLING, handler=self.callback)
        self.expired = utime.ticks_ms() + self.period
            
    def callback(self, pin):
        if pin == self.Btn:
            self.WasPressed = True
            self.expired = utime.ticks_ms() + self.period
    
    def In(self):
        now = utime.ticks_ms();
        
        if (now < self.expired):
            if self.WasPressed == True:
                self.WasPressed = False
                return 1
        
        self.WasPressed = False
        
        if (self.Btn.value() == 1):
            return 0
        
        return 1
        
        