from machine import Pin
import time
import BrainPadType
import BrainPadDisplay
import BrainPadAnalog
import BrainPadDigital
import BrainPadServo
import BrainPadNeopixel
import BrainPadSound
import BrainPadButtons
import BrainPadAccel
import BrainPadI2cBus
import BrainPadDistanceSensor
import BasicGraphics
import BrainPadInfrared
import BrainPadTouch


isPulse = BrainPadType.BrainPadType().IsPulse
display = BrainPadDisplay.Display()
 
IsPulse = isPulse

# main API
def In(obj):    
    return obj.In()
            
def Out(obj, oValue):    
    return obj.Out(oValue)

def Wait(sec):
    time.sleep(sec)
    
def Print(s):
    display.Print(s)

# Display
def Show():
    display.Show()    
    
def Clear():
    display.Clear()
    
def Circle(x, y, r):
    display.Circle(x, y, r)
    
def Line(x1, y1, x2, y2):
    display.Line(x1, y1, x2, y2)
    
def Rect(x, y, w, h):
    display.Rect(x, y, w, h)
    
def Point(x, y, c):
    display.Point(x, y, c)
    
def Text(s, x, y):
    display.Text(s, x, y)
    
def TextEx(s, x, y, hscale, vscale):
    display.TextEx(s, x, y, hscale, vscale)
    
def CreateImage(width, height, data, hScale, vScale, transform):
    return display.CreateImage(width,height,data, hScale, vScale, transform)

def Image(img, x, y):
    return display.CreateImage(img,x,y)

def Color(c):
    return display.Color(c)

def CreateImage(width, height, data, hScale = 1, vScale = 1, transform = 0):
    return display.CreateImage(width, height, data, hScale, vScale, transform)

def Image(image, x, y):
    display.Image(image, x, y)
    
def Touch(pin, sensitiveLevel):
    return BrainPadTouch.Touch(pin, sensitiveLevel)

def Analog(pin):
    return BrainPadAnalog.Analog(pin)

def Digital(pin):
    return BrainPadDigital.Digital(pin)

def Buttons(pin, detectPeriod):
    return BrainPadButtons.Buttons(pin, detectPeriod)

def Accel(xyz):
    return BrainPadAccel.Accel(xyz)

def DistanceSensor(triggerPin, echoPin):
    return BrainPadDistanceSensor.DistanceSensor(triggerPin, echoPin)

def I2cBus(address):
    return BrainPadI2cBus.I2cBus(address)
    
def Infrared(pin):
    return BrainPadInfrared.Infrared(pin)

def Neopixel(pin, lednum):
    return BrainPadNeopixel.Neopixel(pin, lednum)

def Servo(pin):
    return BrainPadServo.Servo(pin)

def Sound(pin, playtime, volume):
    return BrainPadSound.Sound(pin, playtime, volume)

    

        
    
    
    
    
    
        
