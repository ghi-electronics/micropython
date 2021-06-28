import machine
from machine import Pin
from hcsr04 import HCSR04
import BrainPad

class DistanceSensor:                    
    def __init__(self, triggerPin, echoPin):
        self.trigger = BrainPad.BrainPad.GetPinFromString(triggerPin)
        self.echo = BrainPad.BrainPad.GetPinFromString(echoPin)
        self.sensor = HCSR04(self.trigger, self.echo)
            
    def In(self):
        value = self.sensor.distance_cm()
        return value

