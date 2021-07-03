import pyb
import machine
from machine import ADC
from machine import Pin
from BrainPadUtil import *

class Analog:
        
    def ConvertPinToPwmTimer(self):        
        timer = GetPwmTimerFromPin(self.pin)
        return timer
    
    def ConvertPinToPwmChannel(self):        
        channel = GetPwmChannelFromPin(self.pin)        
        return channel
        
    def __init__(self, pin):
        self.pin = GetPinFromString(pin)
        
    def In(self):            
        analogIn = pyb.ADC(self.pin)
        return analogIn.read() * 3.3 / 4096
    
    def Out(self, value):        
        self.timer = pyb.Timer(self.ConvertPinToPwmTimer(), freq=1000)
        self.channel = self.timer.channel(self.ConvertPinToPwmChannel(), pyb.Timer.PWM, pin=Pin(self.pin))
        self.channel.pulse_width_percent(value)
        
            