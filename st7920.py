from machine import Pin, SPI
from time import sleep

# dimension framebuffer
rowBound = 64       # bytearray 'rows' - 64 rows -> 64bits
colBound = 128//8   # 'cols' in each bytearray - 16 bytes -> 128bits

""" EXAMPLE WIRING (MCU runs at 3.3V, so use VIN to get 5V)
        * RW    - GPIO13 (Cockle pin7)  - SPI MOSI  
        * E     - GPIO14 (Cockle pin5)  - SPI Clock
        * PSB   - GND                   - Activate SPI
        * RST   - 5V                    - resetDisplay
        * V0    - 5V                    - LCD contrast
        * BLA   - 5V                    - Backlight Anode
        * BLK   - GND                   - Backlight Cathode
        * VCC   - 5V                    - USB power VIN (not 3V3)
        * GND   - 0V
        
    By default, attempts to wire to Hardware SPI as described at https://docs.micropython.org/en/latest/esp8266/esp8266/quickref.html#hardware-spi-bus
"""
class Screen:
    def __init__(self, sck=None, mosi=None, miso=None, spi=None, resetDisplayPin=None, slaveSelectPin=None):
        
        self.cmdbuf = bytearray()
        
        if spi != None:
            self.spi = spi
        else:
            baudrate=8000000
            polarity=1
            phase=0
            if sck or mosi or miso: # any pins are identified
                assert sck and mosi and miso, "All SPI pins sck, mosi and miso need to be specified"
            else:
                # workaround for hardware SPI constructor apparently not working
                sck =  Pin(14, mode=Pin.OUT) # labelled 5 on nodeMCU
                mosi = Pin(13, mode=Pin.OUT) # labelled 7 on nodeMCU
                miso = Pin(12, mode=Pin.IN) # labelled 6 on nodeMCU # not connected, screen has no MISO line
            self.spi = SPI(-1, baudrate=baudrate, polarity=polarity, phase=phase, sck=sck, mosi=mosi, miso=miso)

        # allocate frame buffer just once, use bytearrays for rows
        self.fbuff = [bytearray(colBound) for rowPos in range(rowBound)]
 
        self.resetDisplayPin = resetDisplayPin
        if self.resetDisplayPin is not None:
            self.resetDisplayPin.init(mode=Pin.OUT)
            # reset the display
            self.reset()
        
        self.slaveSelectPin = slaveSelectPin
        if self.slaveSelectPin is not None:
            self.slaveSelectPin.init(mode=Pin.OUT)
            # deselect slave
            self.select(False)

        self.send(0, 0, 0x30)  # basic instruction set
        self.send(0, 0, 0x30)  # repeated
        self.send(0, 0, 0x0C)  # display on

        self.send(0, 0, 0x34)  # enable RE mode
        self.send(0, 0, 0x34)
        self.send(0, 0, 0x36)  # enable graphics display

        self.set_rotation(0)  # rotate to 0 degrees

        self.clear()
        self.redraw()

    # slave select is active low - 0V means active
    def select(self, selected):
        self.slaveSelectPin.value( 0 if selected else 1)
    
    # reset logic untested
    def reset(self):
        # pulse active low to reset screen
        self.resetDisplayPin.value(0)
        sleep(0.1)
        self.resetDisplayPin.value(1)

    def set_rotation(self, rot):
        if rot == 0 or rot == 2:
            self.width = 128
            self.height = 64
        elif rot == 1 or rot == 3:
            self.width = 64
            self.height = 128
        self.rot = rot

    def send(self, rs, rw, cmds):
        #TODO CH MEMORY - PRE-ALLOCATE COMMAND BUFFER BYTEARRAY, OVERWRITE EACH TIME? JUST WRITE BYTES DIRECTLY?
        if self.slaveSelectPin:
            self.select(True)
        if type(cmds) is int:  # if a single arg, convert to a list
            cmds = [cmds]
        b1 = 0b11111000 | ((rw & 0x01) << 2) | ((rs & 0x01) << 1)
        self.cmdbuf[:] = bytearray() # empty cmdbuf
        self.cmdbuf.append(b1)
        for cmd in cmds:
            self.cmdbuf.append(cmd & 0xF0)
            self.cmdbuf.append((cmd & 0x0F) << 4)
        self.spi.write(self.cmdbuf)
        if self.slaveSelectPin:
            self.select(False)

    def clear(self):
        rowPos = 0
        while rowPos < rowBound:
            row = self.fbuff[rowPos]
            colPos = 0
            while colPos < colBound:
                row[colPos]=0
                colPos += 1
            rowPos += 1

    def line(self, x1, y1, x2, y2, set=True):
        diffX = abs(x2 - x1)
        diffY = abs(y2 - y1)
        shiftX = 1 if (x1 < x2) else -1
        shiftY = 1 if (y1 < y2) else -1
        err = diffX - diffY
        drawn = False
        while not drawn:
            self.plot(x1, y1, set)
            if x1 == x2 and y1 == y2:
                drawn = True
                continue
            err2 = 2 * err
            if err2 > -diffY:
                err -= diffY
                x1 += shiftX
            if err2 < diffX:
                err += diffX
                y1 += shiftY

    def fill_rect(self, x1, y1, x2, y2, set=True):
        for y in range(y1, y2 + 1):
            self.line(x1, y, x2, y, set)

    def rect(self, x1, y1, x2, y2, set=True):
        self.line(x1, y1, x2, y1, set)
        self.line(x2, y1, x2, y2, set)
        self.line(x2, y2, x1, y2, set)
        self.line(x1, y2, x1, y1, set)

    def plot(self, x, y, set=True):
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return
        if set:
            if self.rot == 0:
                self.fbuff[y][x // 8] |= 1 << (7 - (x % 8))
            elif self.rot == 1:
                self.fbuff[x][15 - (y // 8)] |= 1 << (y % 8)
            elif self.rot == 2:
                self.fbuff[63 - y][15 - (x // 8)] |= 1 << (x % 8)
            elif self.rot == 3:
                self.fbuff[63 - x][y // 8] |= 1 << (7 - (y % 8))
        else:
            if self.rot == 0:
                self.fbuff[y][x // 8] &= ~(1 << (7 - (x % 8)))
            elif self.rot == 1:
                self.fbuff[x][15 - (y // 8)] &= ~(1 << (y % 8))
            elif self.rot == 2:
                self.fbuff[63 - y][15 - (x // 8)] &= ~(1 << (x % 8))
            elif self.rot == 3:
                self.fbuff[63 - x][y // 8] &= ~(1 << (7 - (y % 8)))

    def redraw(self, dx1=0, dy1=0, dx2=127, dy2=63):
        for i in range(dy1, dy2 + 1):
            self.send(0, 0, [0x80 + i % 32, 0x80 + ((dx1 // 16) + (8 if i >= 32 else 0))])  # set address
            self.send(1, 0, self.fbuff[i][dx1 // 16:(dx2 // 8) + 1])
