import BrainPadType

IsPulse = BrainPadType.BrainPadType().IsPulse


# Util    
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
<<<<<<< HEAD
        return "PA2"
=======
        return "PA5"
>>>>>>> a4930b6ae95534f8557c7bc300e77dca1f532a13
    
    if (pinlower == "p3"):
        if (IsPulse == True):
            return "PA1"
        
    if (pinlower == "p4"):
        if (IsPulse == True):
            return "PA0"
        
    if (pinlower == "p5"):
        if (IsPulse == True):
            return "PA7"
        
    if (pinlower == "p6"):
        if (IsPulse == True):
            return "PA4"
    
    if (pinlower == "p7"):
        if (IsPulse == True):
            return "PB0"
        
    if (pinlower == "p8"):
        if (IsPulse == True):
            return "PA9"
        
    if (pinlower == "p9"):
        if (IsPulse == True):
            return "PB1"
        
    if (pinlower == "p10"):
        if (IsPulse == True):
            return "PA6"
        
    if (pinlower == "p11"):
        if (IsPulse == True):
            return "PB6"
        
    if (pinlower == "p12"):
        if (IsPulse == True):
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
        if (IsPulse == True):
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
    
def Scale(value, originalMin, originalMax, scaleMin, scaleMax):
    scale = (scaleMax - scaleMin) / (originalMax - originalMin)
    ret = (scaleMin + ((value - originalMin) * scale))
    if ret > scaleMax:
        return scaleMax
    if ret < scaleMin:
        return scaleMin        
    return ret