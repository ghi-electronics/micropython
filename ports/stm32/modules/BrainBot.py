from BrainPad import *

GROUND_SENSOR_NONE = const(0)
GROUND_SENSOR_LEFT = const(1)
GROUND_SENSOR_RIGHT = const(2)
GROUND_SENSOR_BOTH = const(3)

class Invert:
    invertLeftMotor = False;
    invertRightMotor = False;

i2cBus = I2cBus(0x01);
sound = Sound(P0, 0.2, 50);
neopixel = Neopixel(P12, 2);
distance = Distance(P16, P15);

leftLineSensor = Digital(P13);            
rightLineSensor = Digital(P14);                 

data5 = bytearray(5)
data4 = bytearray(4)
    
def Beep():
    Out(sound, 1000)
    
def Move(leftSpeed, rightSpeed):
    if (Invert.invertLeftMotor == True):
        leftSpeed = leftSpeed * -1
    
    if (Invert.invertRightMotor == True):
        rightSpeed = rightSpeed * -1
        
    if (leftSpeed < -100 or leftSpeed > 100 or rightSpeed < -100 or rightSpeed > 100):
        raise Exception("Speed must be in range [-100:100]")
    
    data5[0] = 0x02;

    left = int(Scale(leftSpeed, -100, 100, -255, 255))
    right = int(Scale(rightSpeed, -100, 100, -255, 255))
    
    if (left > 0):
        data5[1] = left;
        data5[2] = 0x00;        
    else:
        left = left * -1;
        data5[1] = 0x00;
        data5[2] = left;
    

    if (right > 0):
        data5[3] = right
        data5[4] = 0x00;       
    else :
        right = right* -1
        data5[3] = 0x00
        data5[4] = right
        
    Out(i2cBus, data5)
    
def Stop():
    Move(0,0)
    
def Headlight(color):       
    data4[0] = 0x01
    data4[1] = (color >> 16)
    data4[2] = (color >> 8)
    data4[3] = (color >> 0)
    
    Out(i2cBus, data4)
    
def Taillight(lelfColor, rightColor):
    data2 = [lelfColor, rightColor]
    Out(neopixel, data2)
    
def GroundSensor():
    if (In(leftLineSensor) > 0 and In(rightLineSensor) > 0):
        return GROUND_SENSOR_NONE    
    else:
        if (In(leftLineSensor) > 0):
            return GROUND_SENSOR_LEFT
        else:
            if (In(rightLineSensor) > 0):
                return GROUND_SENSOR_RIGHT;
    
    return GROUND_SENSOR_BOTH;
    
def DistanceSensor():
    return In(distance)

def InvertLeftMotor():
    Invert.invertLeftMotor = True
    
def InvertRightMotor():
    Invert.invertRightMotor = True
    
        
        
            
            
        
    
    
    













    




  
  










