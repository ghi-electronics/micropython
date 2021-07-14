import BrainPadType
import machine
from machine import Pin, I2C
import time
import ssd1306
import TickLedMatrix
import BasicGraphics
import BrainPadType

class Display:
    
    def __init__(self):
        self.color = 1

        if BrainPadType.BrainPadType.IsPulse == False:
            self.tickGfx = TickLedMatrix.TickMatrixController()            
        else:
            self.width = 128
            self.heigh = 64
            self.pulseGfx = BasicGraphics.BasicGraphics(self.width, self.heigh)
            self.InitPulseDisplay()
            self.messages = ["" for x in range(8)]
                        
    def InitPulseDisplay(self):
        self.lcdReset = Pin("PB2",Pin.OUT_PP)
        self.lcdReset.low()
        time.sleep(0.05)
        self.lcdReset.high()
        
        i2c = I2C(2)
        self.pulseLcd = ssd1306.SSD1306_I2C(self.width, self.heigh, i2c)
        
    def SetBrightness(self, brightness):
        if BrainPadType.BrainPadType.IsPulse == False:
            self.tickGfx.SetBrightness(brightness)
        
    def Clear(self):
        if BrainPadType.BrainPadType.IsPulse == False:
            self.tickGfx.Clear()
        else:
            self.pulseLcd.fill(0)
            self.pulseGfx.Clear()            
            
    def Show(self):
        if BrainPadType.BrainPadType.IsPulse == False:
             self.tickGfx.Show()
        else:
            for y in range(self.heigh):
                for x in range (self.width):
                    index = int(y * self.width + x)
                    self.pulseLcd.pixel(x, y, self.pulseGfx.buffer[index])
                                   
            self.pulseLcd.show()
            
    def Print(self, v):
        if (type(v) is str):
            s = v
        else:
            s = str(v)
            
        self.Clear()
        
        if BrainPadType.BrainPadType.IsPulse == False:
            self.tickGfx.DrawText(s)
        else:
            self.pulseGfx.Clear();
            
            for i in range(7):
                self.messages[i] = self.messages[i + 1]
            
            self.messages[7] = s
                
            for i in range(8):                
                self.pulseGfx.DrawString(self.messages[i], self.color, 0, i * 8)
            
        self.Show()
    
    def Circle(self, x, y, radius):
        if BrainPadType.BrainPadType.IsPulse == False:
            self.tickGfx.DrawCircle(self.color, x, y, radius)
        else:
            self.pulseGfx.DrawCircle(self.color, x, y, radius)
                
    def Line(self, x1, y1, x2, y2):
        if BrainPadType.BrainPadType.IsPulse == False:
            self.tickGfx.DrawLine(self.color, x1, y1, x2, y2)
        else:
            self.pulseGfx.DrawLine(self.color, x1, y1, x2, y2)
            
    def Rect(self, x, y, w, h):
        if BrainPadType.BrainPadType.IsPulse == False:
            self.tickGfx.DrawRectangle(self.color, x, y, w, h)
        else:
            self.pulseGfx.DrawRectangle(self.color, x, y, w, h)
            
    def FillRect(self, x, y, w, h):
        w = w + x
        h = h + y
        
        for h1 in range(y,h):
            for w1 in range(x,w):
                self.Point(w1, h1, self.color)
            
            
    def Point(self, x, y, c):
        if BrainPadType.BrainPadType.IsPulse == False:
            self.tickGfx.SetPixel(x, y, c)
        else:
            self.pulseGfx.SetPixel(x, y, c)
            
    def Text(self, v, x, y):
        if (type(v) is str):
            s = v
        else:
            s = str(v)
            
        if BrainPadType.BrainPadType.IsPulse == False:
            self.tickGfx.DrawText(s)
        else:
            self.pulseGfx.DrawString(s, self.color, x, y)
            
    def TextEx(self, v, x, y, xscale, yscale):
        if (type(v) is str):
            s = v
        else:
            s = str(v)

        if BrainPadType.BrainPadType.IsPulse == False:
            self.tickGfx.DrawText(s)
        else:            
            self.pulseGfx.DrawString(s, self.color, x, y, xscale, yscale)
             
    def Color(self, c):
        self.color = c
        
    def CreateImage(self, width, height, data, hScale = 1, vScale = 1, transform = BasicGraphics.Image.NoTransform):
        if BrainPadType.BrainPadType.IsPulse == False:
            hScale = 1
            vScale = 1

        self.image = BasicGraphics.Image(data, width, height, hScale, vScale, transform)
        return self.image
    
    def Image(self, image, x, y):
        if BrainPadType.BrainPadType.IsPulse == False:
            self.tickGfx.DrawImage(image, x, y)
        else:
            self.pulseGfx.DrawImage(image, x, y)
                            