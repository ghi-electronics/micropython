import machine
from machine import Pin, I2C
import MC3216Controller
import BrainPadType

class Accel:
    def __init__(self, xyz):
        self.doX = False
        self.doY = False
        self.doZ = False
        
        xyz = xyz.lower()
        
        if xyz == 'x':
            self.doX = True
            
        if xyz == 'y':
            self.doY = True
            
        if xyz == 'z':
            self.doZ = True
            
        if (self.doX == False and self.doY == False and self.doZ == False):
            raise Exception("Must be x or y or z!")    
            
        if BrainPadType.BrainPadType.IsPulse == True:
            self.i2c = I2C(2, freq=100000)
            self.accel = MC3216Controller.MC3216Controller(self.i2c)
        
    def In(self):
        if self.doX == True:
            return self.GetX()
        
        if self.doY == True:
            return self.GetY()
        
        if self.doZ == True:
            return self.GetZ()
        
    def GetX(self):
        if BrainPadType.BrainPadType.IsPulse == True:
            x = self.accel.GetX()             
            return (x + 128) / 256
        return 0
    
    def GetY(self):
        if BrainPadType.BrainPadType.IsPulse == True:
            y = self.accel.GetY()             
            return (y + 128) / 256
        return 0
    
    def GetZ(self):
        if BrainPadType.BrainPadType.IsPulse == True:
            z = self.accel.GetZ()             
            return (z + 128) / 256
        return 0