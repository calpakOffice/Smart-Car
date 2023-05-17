from rpi_lcd import LCD

class LcdI2CWriter:
    def __init__(self):
        self.lcd = LCD()
    

    def Write(self,text ,line):
        self.lcd.text(text, line)

    def Clear(self):
        self.lcd.clear()
