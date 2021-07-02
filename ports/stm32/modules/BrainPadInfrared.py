import machine
from machine import Pin
from utime import ticks_us,ticks_diff
import pyb
from BrainPadUtil import *

def GetKeyInTableMap(key):
            
    if key == 0: # Power off
        return 10

    if key == 2: # Power on
        return 11

    if key == 1: # Up
        return 12

    if key == 9: # Down
        return 13

    if key == 4: # left
        return 14

    if key == 6: # right
        return 15

    if key == 5: # Center
        return 16

    if key == 8: # Back
        return 17

    if key == 10: # Next
        return 18

    if key == 12: # Plus
        return 19

    if key == 14: # Minus
        return 20

    if key == 13: # 0
        return 0

    if key == 16 or key == 17 or key == 18: #1,2,3    
        return key - 15

    if key == 20 or  key == 21 or key == 22 : # 4,5,6
        return key - 16

    if key == 24 or key == 25 or key == 26: # 7,8,9
        return key - 17


    return PRESS_CODE_NONE

class Infrared:
        
    PreBurst = const(0)
    PostPreBurst = const(1)
    RepeatEnd = const(2)
    BurstBit = const(3)
    DataBit = const(4)
                
    BurstPreTime = const(9000)
    SpacePreTime = const(4500)
    BurstBitTime = const(562)
    ZeroBitTime = const(562)
    OneBitTime = const(1688)
    RepeatTime = const(2250)
    RepeatEndTime = const(562)
    
    MaxKey = const(10)
    
    PRESS_CODE_NONE = const(100)
    
    def __init__(self, pin):        
        self.pin = Pin(GetPinFromString(pin),Pin.IN)
        self.pin.irq(trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING, handler=self.callback)
        self.last_us = 0
        self.us = 0
        self.status = PreBurst
        self.necMessage = 0
        self.bitIndex = 0
        self.ErrorCounter = 0
        self.keyArrayIndex = 0
        self.keyArray = bytearray(MaxKey)
        self.lowMargin = 0.8
        self.highMargin = 1.2        
        
    def In(self):               
        if self.keyArrayIndex > 0:            
            self.keyArrayIndex -= 1
            return GetKeyInTableMap(self.keyArray[self.keyArrayIndex])
        else:
            return PRESS_CODE_NONE
        
    def InRange(self, value, expected):
        if ((value > (expected * self.lowMargin)) and (value < (expected * self.highMargin))):
            return True
        else:
            return False
            
        
    def callback(self, pin):        
        #t = ticks_us()
        bitTime = (ticks_us() - self.last_us)
        self.last_us = ticks_us()           

        if self.status == PreBurst:
            if self.InRange(bitTime, BurstPreTime):
                self.status = PostPreBurst
                self.necMessage = 0
                self.bitIndex = 0
                
            return
        
        if self.status == PostPreBurst:
            if self.InRange(bitTime, SpacePreTime):
                self.status = BurstBit
            else:
                if self.InRange(bitTime, RepeatTime):
                    self.status = RepeatEnd
                else:
                    self.ErrorCounter += 1
                    self.status = PreBurst
                    #print("Error PostPreBurst")
            
            return
        
        if self.status == RepeatEnd:
            if self.InRange(bitTime, RepeatEndTime):
                return
            else:
                self.ErrorCounter +=1
                self.status = PreBurst
                #print("Error RepeatEnd")
                
            return
        
        if self.status == BurstBit:
            if self.InRange(bitTime, BurstBitTime):
                self.status = DataBit
            else:
                self.ErrorCounter +=1
                self.status = PreBurst
                #print("Error BurstBit")
            
            return
                
        if self.status == DataBit:
            self.status = BurstBit
            
            if self.InRange(bitTime, ZeroBitTime):                    
                self.bitIndex += 1
            else:
                if self.InRange(bitTime, OneBitTime):                        
                    self.necMessage |= ((1 << self.bitIndex))
                    self.bitIndex += 1
                else:
                    self.ErrorCounter +=1
                    self.status = PreBurst
                    #print("Error DataBit")
                    
            if self.bitIndex == 32:
                b0 = (self.necMessage >> 0) & 0xFF
                b1 = ~(self.necMessage >> 8) & 0xFF
                b2 = (self.necMessage >> 16) & 0xFF
                b3 = ~(self.necMessage >> 24) & 0xFF
                                    
                if (b0 == b1 and b2 == b3):
                    if self.keyArrayIndex < MaxKey:
                        self.keyArray[self.keyArrayIndex] = b2
                        self.keyArrayIndex +=1
                                
                self.status = PreBurst
                
            
            return
        
        self.status = PreBurst        
        
                
                        
                        
                    
                    

            
            
            
    