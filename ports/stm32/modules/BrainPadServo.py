import pyb
import machine
from machine import Pin
import time
import BrainPad

class Servo:                    
    def ConvertPinToPwmTimer(self):        
        timer = BrainPad.BrainPad.GetPwmTimerFromPin(self.pin)
        return timer
    
    def ConvertPinToPwmChannel(self):        
        channel = BrainPad.BrainPad.GetPwmChannelFromPin(self.pin)        
        return channel
    
    def __init__(self, pin):
        self.pin = BrainPad.BrainPad.GetPinFromString(pin)
        self.ConfigurePulseParameters(0.5, 2.4)
        self.ConfigureAsPositional(False)
        self.EnsureFrequency()
                    
    def ConfigurePulseParameters(self, minimumPulseWidth, maximumPulseWidth):
        self.minPulseLength = minimumPulseWidth
        self.maxPulseLength = maximumPulseWidth
    
    def ConfigureAsPositional(self, inverted):
        self.invertServo = inverted
        
    def EnsureFrequency(self):
        self.timer = pyb.Timer(self.ConvertPinToPwmTimer(), freq=50)
        self.channel = self.timer.channel(self.ConvertPinToPwmChannel(), pyb.Timer.PWM, pin=Pin(self.pin))
        
    def Set(self, value):
        self.FixedSetPosition(value)    
        
    def Stop(self):
        self.channel.pulse_width_percent(0)
       
    def FixedSetPosition(self, position):
        if (position < 0 or position > 180):
            print("invalid position")
    
        self.EnsureFrequency()
        
        if self.invertServo == True:
            position = 180 - position
            
        duty = ((position / 180.0) * (self.maxPulseLength / 20 - self.minPulseLength / 20)) + self.minPulseLength / 20
        
        duty = duty*100
        
        print(duty)
        
        self.channel.pulse_width_percent(duty)
        
    def Out(self, position):
        self.FixedSetPosition(position)
        
    
    
        
    
            
            
                
            
             
            
            
            
            
    
        