import BrainPadType

IsPulse = BrainPadType.BrainPadType().IsPulse

PinMapPulse = [
"PA5", #P0
"PA3", #P1
"PA2", #P2
"PA1", #P3
"PA0", #P4
"PA7", #P5
"PA4", #P6
"PB0", #P7
"PA9", #P8
"PB1", #P9
"PA6", #P10
"PB6", #P11
"PA10", #P12
"PB3", #P13
"PB4", #P14
"PB5", #P15
"PB12", #P16
"-1" , #P17
"-1" , #P18
"PB10", #P19
"PB11", #P20
"PA8", #LED
"PB8", #BUZZER
"PC13", #A
"PB7" #B
]

PinMapTick = [
"PA5", #P0
"PA3", #P1
"PA2", #P2
"-1", #P3
"-1", #P4
"-1", #P5
"-1", #P6
"-1", #P7
"-1", #P8
"-1", #P9
"-1", #P10
"-1", #P11
"PA5", #P12
"PB3", #P13
"PB4", #P14
"PB5", #P15
"PA3", #P16
"-1", #P17
"-1", #P18
"PB10", #P19
"PB11", #P20
"PA8", #LED
"PB8", #BUZZER
"PC13", #A
"PB7" #B    
]   


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

def GetPinFromObject(pin):
    if (type(pin) is str):
        return GetPinFromString(pin)
    else:
        return GetPinFromInt(pin)
                
def GetPinFromInt(pin):        
    if (IsPulse == True):
        return PinMapPulse[pin]

    return PinMapTick[pin]
    
def GetPinFromString(pin):
    return "-1"
    
def Scale(value, originalMin, originalMax, scaleMin, scaleMax):
    scale = (scaleMax - scaleMin) / (originalMax - originalMin)
    ret = (scaleMin + ((value - originalMin) * scale))
    if ret > scaleMax:
        return scaleMax
    if ret < scaleMin:
        return scaleMin        
    return ret