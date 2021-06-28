from machine import Pin, I2C

class I2cBus:
    def __init__(self, address):
        self.i2cControl = I2C(4, freq=100000)
        self.SlaveAddress = address        
         
    def In(self):
        return self.i2cControl.readfrom(self.SlaveAddress, 1)
    
    def Out(self, buff):                                
        self.i2cControl.writeto(self.SlaveAddress, buff)
        
    
    