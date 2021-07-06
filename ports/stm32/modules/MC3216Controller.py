import machine
from machine import Pin, Timer, I2C
from micropython import const
import time

MC3216_Mode = const(0x07)
MC3216_Opstat = const(0x04)
MC3216_Outcfg = const(0x20)
MC3216_XOut = const(0x0D)
MC3216_YOut = const(0x0F)
MC3216_ZOut = const(0x11)
MC3216_SRTFR = const(0x08)
SlaveAddress = const(0x4C)

class MC3216Controller:
    def __init__(self, i2c):
        
        self.i2c = i2c
        
        self.WriteToRegister(MC3216_Outcfg, 2)
        self.WriteToRegister(MC3216_Mode, 1)
        
        read = self.ReadFromRegister(MC3216_Opstat, 1)

        if (read[0] & 0x01) != 0x01:
            raise Exception("Unexpected init!")    
        
    def WriteToRegister(self, reg, data):
        count = 2
        buf = bytearray(2)        
        buf[0] = reg;
        buf[1] = data;                
        self.i2c.writeto(SlaveAddress, buf)
        
    def ReadFromRegister(self, reg, count):
        return self.i2c.readfrom_mem(SlaveAddress,reg, count)
    
    def GetX(self):
        reg = self.ReadFromRegister( MC3216_XOut, 1)
        return int(reg[0])
    
    def GetY(self):
        reg = self.ReadFromRegister( MC3216_YOut, 1)
        return int(reg[0])
    
    def GetZ(self):
        reg = self.ReadFromRegister( MC3216_ZOut, 1)
        return int(reg[0])

