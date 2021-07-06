from machine import Pin
import pyb
import time
import BasicGraphics

class TickMatrixController(BasicGraphics.BasicGraphics):
    def __init__(self):
        self.white = 1
        
        self.pin = Pin('PA9')
        self.tim = pyb.Timer(1, freq=1000)
        self.brightnessChannel = self.tim.channel(2, pyb.Timer.PWM, pin=self.pin)
        self.brightnessChannel.pulse_width_percent(50)
 
        self.ledMatrix = [
            Pin("PB14",Pin.OUT_PP),
            Pin("PA10",Pin.OUT_PP),
            Pin("PA14",Pin.OUT_PP),
            Pin("PA15",Pin.OUT_PP),
            Pin("PA8",Pin.OUT_PP),
            
            Pin("PB13",Pin.OUT_PP),
            Pin("PB15",Pin.OUT_PP),
            Pin("PB6",Pin.OUT_PP),
            Pin("PA13",Pin.OUT_PP),
            Pin("PC14",Pin.OUT_PP),
            
            Pin("PB12",Pin.OUT_PP),
            Pin("PB2",Pin.OUT_PP),
            Pin("BOOT0",Pin.OUT_PP),
            Pin("PC15",Pin.OUT_PP),
            Pin("PB8",Pin.OUT_PP),
            
            Pin("PB1",Pin.OUT_PP),
            Pin("PB0",Pin.OUT_PP),
            Pin("PA4",Pin.OUT_PP),
            Pin("PH1",Pin.OUT_PP),
            Pin("PB9",Pin.OUT_PP),
            
            Pin("PA7",Pin.OUT_PP),
            Pin("PA6",Pin.OUT_PP),
            Pin("PA1",Pin.OUT_PP),
            Pin("PA0",Pin.OUT_PP),
            Pin("PH0",Pin.OUT_PP)
            ]
        for pin in range(len(self.ledMatrix)):
            self.ledMatrix[pin].low()
    
    def SetBrightness(self, brightness):
        self.brightnessChannel.pulse_width_percent(brightness)
        
    def SetPixel(self, x, y, color):
        if (x < 0 or x > 4):
            return 0
        if (y < 0 or y > 4):
            return 0
        
        index = (y * 5) + x
        
        if color != 0:
            self.ledMatrix[index].high()
        else:
            self.ledMatrix[index].low()
            
    def Clear(self):
        for pin in range(len(self.ledMatrix)):
            self.ledMatrix[pin].low()
            
    def DrawText(self, text):
        if len(text) == 1:
            super().DrawTinyCharacter(ord(text[0]), self.white, 0, 0, True)
        else:
            length = len(text) * 6
            for x in reversed(range(-length, 5+1)):
                super().DrawTinyString(text, self.white, x, 0, True)
                time.sleep(0.08)
            
        
            
        