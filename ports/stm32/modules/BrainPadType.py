import machine
from machine import Pin

class BrainPadType:
    IsPulse = False
    
    def __init__(self):
        pb15 = Pin("PB15",Pin.IN, Pin.PULL_DOWN)
        
        if pb15.value() == 1:
            BrainPadType.IsPulse = True
            
        del pb15
            