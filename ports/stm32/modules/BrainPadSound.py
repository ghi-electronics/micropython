import pyb
import machine
from machine import Pin
import time
from BrainPadUtil import *

class Sound:
    def ConvertPinToPwmTimer(self):        
        timer = GetPwmTimerFromPin(self.pin)
        return timer
    
    def ConvertPinToPwmChannel(self):        
        channel = GetPwmChannelFromPin(self.pin)        
        return channel
    
    def __init__(self, pin, playtime, volume):
        if pin == 'builtin':            
            self.pin = "PB8"
        else:
            self.pin = GetPinFromString(pin)

        self.playTime = playtime
        self.volume = Sound.Scale(volume, 0, 100, 0, 50)      
                    
    def Out(self, value):        
        self.timer = pyb.Timer(self.ConvertPinToPwmTimer(), freq=value)
        self.channel = self.timer.channel(self.ConvertPinToPwmChannel(), pyb.Timer.PWM, pin=Pin(self.pin))
        self.channel.pulse_width_percent(self.volume)
        print(self.volume)
        if value != 0:        
            time.sleep(self.playTime)
            self.channel.pulse_width_percent(0)
            
    def Scale(value, originalMin, originalMax, scaleMin, scaleMax):
        scale = (scaleMax - scaleMin) / (originalMax - originalMin)
        ret = (scaleMin + ((value - originalMin) * scale))
        if ret > scaleMax:
            return scaleMax
        if ret < scaleMin:
            return scaleMin        
        return ret
            
            
                
            
             
            
            
            
            
    
        