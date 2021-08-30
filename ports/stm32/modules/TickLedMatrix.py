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
        self.buffer = bytearray(25)
 
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
    
    def Brightness(self, bright):
        self.brightnessChannel.pulse_width_percent(bright)
        
    def SetPixel(self, x, y, color):
        if (x < 0 or x > 4):
            return 0
        if (y < 0 or y > 4):
            return 0
        
        _x = int(x)
        _y = int(y)
        
        index = (_y * 5) + _x
        
        self.buffer[int(index)] = (color & 0xFF);
        
        #if color != 0:
            #self.ledMatrix[index].high()
        #else:
            #self.ledMatrix[index].low()
        
    def Show(self):
        for index in range(len(self.buffer)):
            if self.buffer[index] != 0:
                self.ledMatrix[index].high()
            else:
                self.ledMatrix[index].low()
                
    def Clear(self):
        self.buffer = bytearray(25)
        #for pin in range(len(self.ledMatrix)):
            #self.ledMatrix[pin].low()
        
    def DrawImage(self, img, x, y):
        super().DrawImage(img, x, y)
            
    def DrawCircle(self, color, x, y, radius):
        super().DrawCircle(color, x, y, radius)
        
    def DrawLine(self, color, x1, y1, x2, y2):
        super().DrawLine(color, x1, y1, x2, y2)
        
    def DrawRectangle(self, color, x, y, width, height):
        super().DrawRectangle(color, x, y, width, height)
        
    def DrawText(self, text):
        if len(text) == 1:
            super().DrawTinyCharacter(ord(text[0]), self.white, 0, 0, True)
        else:
            length = len(text) * 6
            for x in reversed(range(-length, 5+1)):
                super().DrawTinyString(text, self.white, x, 0, True)
                self.Show()
                time.sleep(0.08)
            
        
            
        