import machine
from machine import Pin
from hcsr04 import HCSR04
from BrainPadUtil import *

class DistanceSensor:                    
    def __init__(self, triggerPin, echoPin):
        self.trigger = GetPinFromString(triggerPin)
        self.echo = GetPinFromString(echoPin)
        self.sensor = HCSR04(self.trigger, self.echo)
            
    def In(self):
        value = self.sensor.distance_cm()
        return value

