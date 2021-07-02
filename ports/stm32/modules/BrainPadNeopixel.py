import machine
from machine import Pin
from BrainPadUtil import *
import neopixel

class Neopixel:                    
    def __init__(self, pin, lednum):
        self.pin = GetPinFromString(pin)
        self.num = lednum
        self.neo = neopixel.NeoPixel(machine.Pin(self.pin), self.num)            
    
    def Out(self, color):
        if (type(color) is int):
            for i in range(self.num):
                r = (color >> 16) & 0xFF
                g = (color >> 8) & 0xFF
                b = (color >> 0) & 0xFF
                self.neo[i] =  (r,g,b)                                                       
        else:
            for i in range(len(color)):
                r = (color[i] >> 16) & 0xFF
                g = (color[i] >> 8) & 0xFF
                b = (color[i] >> 0) & 0xFF
                self.neo[i] =  (r,g,b) 
                
        self.neo.write()  
        
            
            
            
            
    
        