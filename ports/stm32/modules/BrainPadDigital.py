import machine
from machine import Pin
import BrainPad

class Digital:                    
    def __init__(self, pin):
        self.pin = BrainPad.BrainPad.GetPinFromString(pin)
        self.pull = "pullup"
            
    def In(self):
        if (self.pull == "pullup"):
            pin = Pin(self.pin, Pin.IN, Pin.PULL_UP)
            return pin.value()
        
        if (self.pull == "pulldown"):
            pin = Pin(self.pin, Pin.IN, Pin.PULL_DOWN)
            return pin.value()
        
        pin = Pin(self.pin, Pin.IN)
        return pin.value()
        
    
    def Out(self, state):
        pin = Pin(self.pin, Pin.OUT)

        if state == True:
            pin.high()
        else:
            pin.low()
            
            
            
            
    
        