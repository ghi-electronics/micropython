import pyb
import machine
from machine import ADC
from machine import Pin
import BrainPad

class Analog:
        
    def ConvertPinToPwmTimer(self):        
        timer = BrainPad.BrainPad.GetPwmTimerFromPin(self.pin)
        return timer
    
    def ConvertPinToPwmChannel(self):        
        channel = BrainPad.BrainPad.GetPwmChannelFromPin(self.pin)        
        return channel
        
    def __init__(self, pin):
        self.pin = BrainPad.BrainPad.GetPinFromString(pin)
        
    def In(self):            
        analogIn = pyb.ADC(self.pin)
        return analogIn.read() * 3.3 / 4096
    
    def Out(self, value):        
        self.timer = pyb.Timer(self.ConvertPinToPwmTimer(), freq=1000)
        self.channel = self.timer.channel(self.ConvertPinToPwmChannel(), pyb.Timer.PWM, pin=Pin(self.pin))
        self.channel.pulse_width_percent(value)
        
            