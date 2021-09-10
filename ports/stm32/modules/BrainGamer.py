from BrainPad import *

class GamerButton:
    buttonScanTime = 0.25;    
    buttonUp = Button(P14, buttonScanTime);
    buttonDown = Button(P15, buttonScanTime);
    buttonLeft = Button(P13, buttonScanTime);
    if IsPulse==True:
        buttonRight = Button(P16, buttonScanTime);
    else:
        buttonRight = Digital(P16);

def ButtonScanTime(value):
    GamerButton.buttonScanTime = value    
    GamerButton.buttonUp = Button(P14, value);
    GamerButton.buttonDown = Button(P15, value);
    GamerButton.buttonLeft = Button(P13, value);
    GamerButton.buttonRight = Button(P16, value);
    
if IsPulse==True:
    rockerX = Analog(P4);
    rockerY = Analog(P3);
    motor = Digital(P8);
    sound = Sound(P0, 0, 50);
    
def Beep():
    if IsPulse==True:
        Out(sound, 1000)
        Wait(0.2)
        Out(sound, 0)
    
def SoundOn(frequency = 1000):
    if IsPulse==True:
        Out(sound, frequency)
    
def SoundOff():
    if IsPulse==True:
        Out(sound, 0)
    
def ButtonUp():
    return In(GamerButton.buttonUp) != 0;

def ButtonDown():
    return In(GamerButton.buttonDown) != 0;

def ButtonLeft():
    return In(GamerButton.buttonLeft) != 0;

def ButtonRight():
    if IsPulse==True:
        return In(GamerButton.buttonRight) != 0;
    else:
        return In(GamerButton.buttonRight) == 0;
    
def RockerX():
    if IsPulse==True:
        return In(rockerX)
    else:
        return 0

def RockerY():
    if IsPulse==True:
        return In(rockerY)
    else:
        return 0

def VibrateOn():
    if IsPulse==True:
        Out(motor, 0);
    
def VibrateOff():
    if IsPulse==True:
        Out(motor, 1);
    
    
    
        
        
            
            
        
    
    
    













    




  
  










