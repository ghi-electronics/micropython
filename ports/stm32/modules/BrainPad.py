from machine import Pin,I2C
import time
import utime
import pyb
import machine
from utime import ticks_us,ticks_diff
import BrainPadType
import BasicGraphics
import BrainPadDisplay
import MC3216Controller
from machine import ADC
from hcsr04 import HCSR04
import neopixel
from stm import pulsefeedback_read

from BrainPadUtil import *

P0 = const(0)
P1 = const(1)
P2 = const(2)
P3 = const(3)
P4 = const(4)
P5 = const(5)
P6 = const(6)
P7 = const(7)
P8 = const(8)
P9 = const(9)
P10 = const(10)
P11 = const(11)
P12 = const(12)
P13 = const(13)
P14 = const(14)
P15 = const(15)
P16 = const(16)
P19 = const(19)
P20 = const(20)

IsPulse = BrainPadType.BrainPadType().IsPulse
IsTick = (IsPulse == False)

# main API
def In(obj):    
    return obj.In()
            
def Out(obj, oValue):    
    return obj.Out(oValue)

def Wait(sec):
    time.sleep(sec)
    
def Print(s):
    Display.Print(s)

# Display
def Brightness(bright):
    Display.Brightness(bright)
    
def Show():
    Display.Show()    
    
def Clear():
    Display.Clear()
    
def Circle(x, y, r):
    Display.Circle(x, y, r)
    
def Line(x1, y1, x2, y2):
    Display.Line(x1, y1, x2, y2)
    
def Rect(x, y, w, h):
    Display.Rect(x, y, w, h)
    
def FillRect(x, y, w, h):
    Display.FillRect(x, y, w, h)
    
def Point(x, y, c):
    Display.Point(x, y, c)
    
def Text(s, x, y):
    Display.Text(s, x, y)
    
def TextEx(s, x, y, hscale, vscale):
    Display.TextEx(s, x, y, hscale, vscale)
    
def CreateImage(width, height, data, hScale, vScale, transform):
    return Display.CreateImage(width,height,data, hScale, vScale, transform)

def Image(img, x, y):
    return Display.CreateImage(img,x,y)

def Color(c):
    return Display.Color(c)

def CreateImage(width, height, data, hScale = 1, vScale = 1, transform = 0):
    return Display.CreateImage(width, height, data, hScale, vScale, transform)

def Image(image, x, y):
    Display.Image(image, x, y)
    
def Touch(pin, sensitiveLevel):
    return Controller.Touch(pin, sensitiveLevel)

def Analog(pin):
    return Controller.Analog(pin)

def Digital(pin):
    return Controller.Digital(pin)

def Button(pin, detectPeriod):
    return Controller.Button(pin, detectPeriod)

def Accel(xyz):
    return Controller.Accel(xyz)

def Distance(triggerPin, echoPin):
    return Controller.Distance(triggerPin, echoPin)

def I2cBus(address):
    return Controller.I2cBus(address)
    
def Infrared(pin):
    return Controller.Infrared(pin)

def Neopixel(pin, lednum):
    return Controller.Neopixel(pin, lednum)

def Servo(pin):
    return Controller.Servo(pin)

def Sound(pin, playtime, volume):    
    return Controller.Sound(pin, playtime, volume)

class Controller:
    class Sound:
        def ConvertPinToPwmTimer(self):        
            timer = GetPwmTimerFromPin(self.pin)
            return timer
        
        def ConvertPinToPwmChannel(self):        
            channel = GetPwmChannelFromPin(self.pin)        
            return channel
        
        def __init__(self, pin, playtime, volume):
            if pin == 'buzzer' or pin == 'BUZZER':            
                self.pin = "PB8"
            else:
                self.pin = GetPinFromObject(pin)

            self.playTime = playtime
            self.volume = Scale(volume, 0, 100, 0, 50)      
                        
        def Out(self, value):        
            self.timer = pyb.Timer(self.ConvertPinToPwmTimer(), freq=value)
            self.channel = self.timer.channel(self.ConvertPinToPwmChannel(), pyb.Timer.PWM, pin=Pin(self.pin))
            self.channel.pulse_width_percent(self.volume)
            
            if value != 0:        
                time.sleep(self.playTime)
                self.channel.pulse_width_percent(0)
                
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
                if (x > 127):
                    x = x - 256
                                    
                d = x * 1.56
                return int(d)
            return 0
        
        def GetY(self):
            if BrainPadType.BrainPadType.IsPulse == True:
                y = self.accel.GetY()             
                if (y > 127):
                    y = y - 256
                    
                d = y * 1.56
                return int(d)
            return 0    
        
        def GetZ(self):
            if BrainPadType.BrainPadType.IsPulse == True:
                z = self.accel.GetZ()             
                if (z > 127):
                    z = z - 256
                    
                d = z * 1.56
                return int(d)
            return 0 
        
    class Touch:
        def __init__(self, pin, sensitiveLevel):
            self.pin =  Pin(GetPinFromObject(pin))
            self.sensitive = 100 - sensitiveLevel
            
        def In(self):
            t = pulsefeedback_read(self.pin)
            scale =  Scale(t, 6, 14, 0, 100)
            
            if (scale >= self.sensitive):
                return 1
            else:
                return 0
            
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

        IRKey = [10, 12, 11, 0xFF, 14, 16, 15, 0xFF, 17, 13, 18, 0xFF, 19, 0, 20, 0xFF, 1, 2, 3, 0xFF, 4, 5, 6, 0xFF, 7, 8, 9]
        
        def __init__(self, pin):        
            self.pin = Pin(GetPinFromObject(pin),Pin.IN)
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
                return Controller.Infrared.IRKey[self.keyArray[self.keyArrayIndex]]
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
            
    class Analog:        
        def ConvertPinToPwmTimer(self):        
            timer = GetPwmTimerFromPin(self.pin)
            return timer
        
        def ConvertPinToPwmChannel(self):        
            channel = GetPwmChannelFromPin(self.pin)        
            return channel
            
        def __init__(self, pin):
            if pin == "led" or pin == "LED":
                self.pin = "PA8"
            else:                
                self.pin = GetPinFromObject(pin)
            
        def In(self):            
            analogIn = pyb.ADC(self.pin)
            v = analogIn.read() * 3.3 / 4096
            v_scale = int(Scale(v, 0, 1, 0, 100))
            return v_scale
        
        def Out(self, value):        
            self.timer = pyb.Timer(self.ConvertPinToPwmTimer(), freq=1000)
            self.channel = self.timer.channel(self.ConvertPinToPwmChannel(), pyb.Timer.PWM, pin=Pin(self.pin))
            self.channel.pulse_width_percent(value)
            
    class Digital:                    
        def __init__(self, pin):
            if pin == "led" or pin == "LED":
                self.pin = "PA8"
            else:                
                self.pin = GetPinFromObject(pin)            
                
        def In(self):
            pin = Pin(self.pin, Pin.IN, Pin.PULL_UP)                                    
            return pin.value()
            
        
        def Out(self, state):
            pin = Pin(self.pin, Pin.OUT)

            if state == True:
                pin.high()
            else:
                pin.low()
                
    class Button:                    
        def __init__(self, pin, detectPeriod):
            self.pin = GetPinFromObject(pin)
            self.period = detectPeriod * 1000
            self.WasPressed = False        
            self.Btn = Pin(self.pin,Pin.IN, Pin.PULL_UP)        
            self.Btn.irq(trigger=Pin.IRQ_FALLING, handler=self.callback)
            self.expired = utime.ticks_ms() + self.period
                
        def callback(self, pin):
            if pin == self.Btn:
                self.WasPressed = True
                self.expired = utime.ticks_ms() + self.period
        
        def In(self):
            now = utime.ticks_ms();
            
            if (now < self.expired):
                if self.WasPressed == True:
                    self.WasPressed = False
                    return 1
            
            self.WasPressed = False
            
            if (self.Btn.value() == 1):
                return 0
            
            return 1
    
    class Distance:                    
        def __init__(self, triggerPin, echoPin):
            self.trigger = GetPinFromObject(triggerPin)
            self.echo = GetPinFromObject(echoPin)
            self.sensor = HCSR04(self.trigger, self.echo)
                
        def In(self):
            value = self.sensor.distance_cm()
            return value
        
    class Neopixel:                    
        def __init__(self, pin, lednum):
            self.pin = GetPinFromObject(pin)
            self.num = lednum
            self.neo = neopixel.NeoPixel(machine.Pin(self.pin), self.num)            
        
        def Out(self, color):
            if (type(color) is int):
                for i in range(self.num):
                    r = (color >> 16) & 0xFF
                    g = (color >> 8) & 0xFF
                    b = (color >> 0) & 0xFF
                    self.neo[i] =  (r,g,b)                                                       
            else:
                for i in range(len(color)):
                    r = (color[i] >> 16) & 0xFF
                    g = (color[i] >> 8) & 0xFF
                    b = (color[i] >> 0) & 0xFF
                    self.neo[i] =  (r,g,b) 
                    
            self.neo.write()
            
    class Servo:                    
        def ConvertPinToPwmTimer(self):        
            timer = GetPwmTimerFromPin(self.pin)
            return timer
        
        def ConvertPinToPwmChannel(self):        
            channel = GetPwmChannelFromPin(self.pin)        
            return channel
        
        def __init__(self, pin):
            self.pin = GetPinFromObject(pin)
            self.ConfigurePulseParameters(0.5, 2.4)
            self.ConfigureAsPositional(False)
            self.EnsureFrequency()
                        
        def ConfigurePulseParameters(self, minimumPulseWidth, maximumPulseWidth):
            self.minPulseLength = minimumPulseWidth
            self.maxPulseLength = maximumPulseWidth
        
        def ConfigureAsPositional(self, inverted):
            self.invertServo = inverted
            
        def EnsureFrequency(self):
            self.timer = pyb.Timer(self.ConvertPinToPwmTimer(), freq=50)
            self.channel = self.timer.channel(self.ConvertPinToPwmChannel(), pyb.Timer.PWM, pin=Pin(self.pin))
            
        def Set(self, value):
            self.FixedSetPosition(value)    
            
        def Stop(self):
            self.channel.pulse_width_percent(0)
           
        def FixedSetPosition(self, position):
            if (position < 0 or position > 180):
                print("invalid position")
        
            self.EnsureFrequency()
            
            if self.invertServo == True:
                position = 180 - position
                
            duty = ((position / 180.0) * (self.maxPulseLength / 20 - self.minPulseLength / 20)) + self.minPulseLength / 20
            
            duty = duty*100        
            
            self.channel.pulse_width_percent(duty)
            
        def Out(self, position):
            self.FixedSetPosition(position)
            
    
    class I2cBus:
        def __init__(self, address):
            self.i2cControl = I2C(4, freq=100000)
            self.SlaveAddress = address        
             
        def In(self):
            return self.i2cControl.readfrom(self.SlaveAddress, 1)
        
        def Out(self, buff):                                
            self.i2cControl.writeto(self.SlaveAddress, buff)
            
class Display:        
    display = BrainPadDisplay.Display()
    
    def Print(s):
        Display.display.Print(s)

    def Brightness(bright):
        Display.display.Brightness(bright)

    def Show():
        Display.display.Show()    
        
    def Clear():
        Display.display.Clear()
        
    def Circle(x, y, r):
        Display.display.Circle(x, y, r)
        
    def Line(x1, y1, x2, y2):
        Display.display.Line(x1, y1, x2, y2)
        
    def Rect(x, y, w, h):
        Display.display.Rect(x, y, w, h)
        
    def FillRect(x, y, w, h):
        Display.display.FillRect(x, y, w, h)
        
    def Point(x, y, c):
        Display.display.Point(x, y, c)
        
    def Text(s, x, y):
        Display.display.Text(s, x, y)
        
    def TextEx(s, x, y, hscale, vscale):
        Display.display.TextEx(s, x, y, hscale, vscale)
        
    def CreateImage(width, height, data, hScale, vScale, transform):
        return Display.display.CreateImage(width,height,data, hScale, vScale, transform)

    def Image(img, x, y):
        return Display.display.CreateImage(img,x,y)

    def Color(c):
        return Display.display.Color(c)

    def CreateImage(width, height, data, hScale = 1, vScale = 1, transform = 0):
        return Display.display.CreateImage(width, height, data, hScale, vScale, transform)

    def Image(image, x, y):
        Display.display.Image(image, x, y)
        
        
                

    

        
    
    
    
    
    
        
