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
        
    def Brightness(self, bright):
        if BrainPadType.BrainPadType.IsPulse == False:
            self.tickGfx.Brightness(bright)
        
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
            self.pulseLcd.blit(self.pulseGfx.buffer1bpp, 0, 0, 0)
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
        _x = int(x)
        _y = int(y)
        if BrainPadType.BrainPadType.IsPulse == False:
            self.tickGfx.DrawCircle(self.color, _x, _y, radius)
        else:
            self.pulseGfx.DrawCircle(self.color, _x, _y, radius)
                
    def Line(self, x1, y1, x2, y2):
        _x1 = int(x1)
        _y1 = int(y1)
        _x2 = int(x2)
        _y2 = int(y2)
        if BrainPadType.BrainPadType.IsPulse == False:
            self.tickGfx.DrawLine(self.color, _x1, _y1, _x2, _y2)
        else:
            self.pulseGfx.DrawLine(self.color, _x1, _y1, _x2, _y2)
            
    def Rect(self, x, y, w, h):
        _x = int(x)
        _y = int(y)
        _w = int(w)
        _h = int(h)
        
        if BrainPadType.BrainPadType.IsPulse == False:
            self.tickGfx.DrawRectangle(self.color, _x, _y, _w, _h)
        else:
            self.pulseGfx.DrawRectangle(self.color, _x, _y, _w, _h)
            
    def FillRect(self, x, y, w, h):
        w = w + x
        h = h + y
        
        _x = int(x)
        _y = int(y)
        _w = int(w)
        _h = int(h)
        
        for h1 in range(_y,_h):
            for w1 in range(_x,_w):
                self.Point(w1, h1, self.color)
            
            
    def Point(self, x, y, c):
        _x = int(x)
        _y = int(y)
        _c = int(c)
        if BrainPadType.BrainPadType.IsPulse == False:
            self.tickGfx.SetPixel(_x, _y, _c)
        else:
            self.pulseGfx.SetPixel(_x, _y, _c)
            
    def Text(self, v, x, y):
        _x = int(x)
        _y = int(y)
        
        if (type(v) is str):
            s = v
        else:
            s = str(v)
            
        if BrainPadType.BrainPadType.IsPulse == False:
            self.tickGfx.DrawText(s)
        else:
            self.pulseGfx.DrawString(s, self.color, _x, _y)
            
    def TextEx(self, v, x, y, xscale, yscale):
        _x = int(x)
        _y = int(y)
        _xscale = int(xscale)
        _yscale = int(yscale)
        
        if (type(v) is str):
            s = v
        else:
            s = str(v)

        if BrainPadType.BrainPadType.IsPulse == False:
            self.tickGfx.DrawText(s)
        else:            
            self.pulseGfx.DrawString(s, self.color, _x, _y, _xscale, _yscale)
             
    def Color(self, c):
        self.color = int(c)
        
    def CreateImage(self, width, height, data, hScale = 1, vScale = 1, transform = BasicGraphics.Image.NoTransform):
        if BrainPadType.BrainPadType.IsPulse == False:
            hScale = 1
            vScale = 1

        _width = int(width)
        _height = int(height)
        _hScale = int(hScale)
        _vScale = int(vScale)
        _transform = int(transform)                
        
        self.image = BasicGraphics.Image(data, _width, _height, _hScale, _vScale, _transform)
        return self.image
    
    def Image(self, image, x, y):
        _x = int(x)
        _y = int(y)
        if BrainPadType.BrainPadType.IsPulse == False:
            self.tickGfx.DrawImage(image, _x, _y)
        else:
            self.pulseGfx.DrawImage(image, _x, _y)
                            