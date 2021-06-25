from machine import Pin
import BrainPadType
import BrainPadDisplay
import time

isPulse = BrainPadType.BrainPadType().IsPulse
display = BrainPadDisplay.Display()


class BrainPad:    
    IsPulse = isPulse
    
    
    def In(obj):
        #if (type(obj) is Analog.Analog):            
        #    return obj.In()
        
        #if (type(obj) is Digital.Digital):            
        #    return obj.In()
        return obj.In()
                
    def Out(obj, oValue):
        #if (type(obj) is Analog.Analog):            
        return obj.Out(oValue)
    
    def Wait(sec):
        time.sleep(sec)

    def Show():
        display.Show()
        
    def Print(s):
        display.Print(s)
        
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
    
    
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # static function
    
    def GetPwmTimerFromPin(pin):
        pinlower = pin
        if (pinlower == "PA8" or pinlower == "PA9" or pinlower == "PA10"):
            return 1
        
        if (pinlower == "PA5" or pinlower == "PA1" or pinlower == "PB10" or pinlower == "PB11"):
            return 2
        
        if (pinlower == "PA2" or pinlower == "PA3"):
            return 15
        
        if (pinlower == "PB8"):
            return 16
        
    def GetPwmChannelFromPin(pin):
        pinlower = pin
        
        if (pinlower == "PA8"):
            return 1
        
        if (pinlower == "PA9"):
            return 2
        
        if (pinlower == "PA10"):
            return 3
        
        if (pinlower == "PA5"):
            return 1
        
        if (pinlower == "PA1"):
            return 2
        
        if (pinlower == "PB10"):
            return 3
        
        if (pinlower == "PB11"):
            return 4
        
        if (pinlower == "PA2"):
            return 1
        
        if (pinlower == "PA3"):
            return 2
        
        if (pinlower == "PB8"):
            return 1
    
    def GetPinFromString(pin):
        pinlower = pin.lower()
        if (pinlower == "p0"):
            return "PA5"
        
        if (pinlower == "p1"):
            return "PA3"
        
        if (pinlower == "p2"):
            return "PA5"
        
        if (pinlower == "p3"):
            if (BrainPad.IsPulse == True):
                return "PA1"
            
        if (pinlower == "p4"):
            if (BrainPad.IsPulse == True):
                return "PA0"
            
        if (pinlower == "p5"):
            if (BrainPad.IsPulse == True):
                return "PA7"
            
        if (pinlower == "p6"):
            if (BrainPad.IsPulse == True):
                return "PA4"
        
        if (pinlower == "p7"):
            if (BrainPad.IsPulse == True):
                return "PB0"
            
        if (pinlower == "p8"):
            if (BrainPad.IsPulse == True):
                return "PA9"
            
        if (pinlower == "p9"):
            if (BrainPad.IsPulse == True):
                return "PB1"
            
        if (pinlower == "p10"):
            if (BrainPad.IsPulse == True):
                return "PA6"
            
        if (pinlower == "p11"):
            if (BrainPad.IsPulse == True):
                return "PB6"
            
        if (pinlower == "p12"):
            if (BrainPad.IsPulse == True):
                return "PA10"
            else:
                return "PA5"
            
        if (pinlower == "p13"):
            return "PB3"
        
        if (pinlower == "p14"):
            return "PB4"
        
        if (pinlower == "p15"):
            return "PB5"
        
        if (pinlower == "p16"):
            if (BrainPad.IsPulse == True):
                return "PB12"
            else:
                return "PA3"
            
        if (pinlower == "p19"):
            return "PB10"
        
        if (pinlower == "p20"):
            return "PB11"
        
        if (pinlower == "a"):
            return "PC13"
        
        if (pinlower == "b"):
            return "PB7"
                
         
            return "-1"
        
    
    
    
    
    
        
