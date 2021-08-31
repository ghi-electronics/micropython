from BrainPad import *

class GamerButton:
    buttonScanTime = 0.25;    
    buttonUp = Button(P14, buttonScanTime);
    buttonDown = Button(P15, buttonScanTime);
    buttonLeft = Button(P13, buttonScanTime);
    buttonRight = Button(P16, buttonScanTime);

def ButtonScanTime(value):
    GamerButton.buttonScanTime = value    
    GamerButton.buttonUp = Button(P14, value);
    GamerButton.buttonDown = Button(P15, value);
    GamerButton.buttonLeft = Button(P13, value);
    GamerButton.buttonRight = Button(P16, value);
    
rockerX = Analog(P4);
rockerY = Analog(P3);
motor = Digital(P8);
sound = Sound(P0, 0, 50);
    
def Beep():
    Out(sound, 1000)
    Wait(0.2)
    Out(sound, 0)
    
def SoundOn(frequency = 1000):
    Out(sound, frequency)
    
def SoundOff():
    Out(sound, 0)
    
def ButtonUp():
    return In(GamerButton.buttonUp) != 0;

def ButtonDown():
    return In(GamerButton.buttonDown) != 0;

def ButtonLeft():
    return In(GamerButton.buttonLeft) != 0;

def ButtonRight():
    return In(GamerButton.buttonRight) != 0;
    
def RockerX():
    return In(rockerX)

def RockerY():
    return In(rockerY)

def VibrateOn():
    Out(motor, 0);
    
def VibrateOff():
    Out(motor, 1);
    
    
    
        
        
            
            
        
    
    
    













    




  
  










