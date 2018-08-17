import board,busio,digitalio,time
from TG_Modules.TG_RGB.rgb import colorst as color # use color to make 
from TG_Modules.TG_RGB.st7735r import ST7735R

#instructions:
"""
1. download:
adafruit_bus_device  -https://github.com/adafruit/Adafruit_CircuitPython_BusDevice
TG_Fonts             -https://github.com/TG-Techie/TG-Fonts
2. nest the TG_RGB and TG_Fonts folders inside of TG_Modules
3. put the TG_Modules folder next to your other libraries
4.hook up the wires as lables in the 'WIRE SECTION'
5.use this as your main.py file
6.keep in mind: it's only a model      ;-)

if you have any questions about this repo i am 'TG-Techie#5402'
on the adafruit discord
"""

#make making digital i/o earier (totally opyional)
def dio(pin, direction = None, init_val = None):
    io = digitalio.DigitalInOut(pin)
    if direction != None:
        if direction:
            io.direction = digitalio.Direction.INPUT
            io.value = init_val
        else:
            io.direction = digitalio.Direction.OUTPUT
            io.value = init_val
    return(io)

#WIRE SECTION
#WIRE SECTION
#WIRE SECTION
#define physical pins to be used
backlight_pin = board.D9
disp_sck = board.SCK
disp_mosi = board.MOSI
disp_miso = board.MISO
disp_cs = board.D8  
disp_dc = board.D7
disp_rst = board.D10
#make the spi object
disp_spi = busio.SPI(clock=board.SCK, MOSI=board.MOSI, MISO=board.MISO)

#start backlight in off position
backlite = dio(backlight_pin,0,False)
backlite.value = False

#setup the display as a car named "disp"
disp = ST7735R(disp_spi, cs=dio(disp_cs),dc=dio(disp_dc),
               rst=dio(disp_rst),rotation = 1)
#LOOK ROTATIONS------------------^^^^^^^^^^^^

#start with black screen then turn on
disp.fill(0)
backlite.value = True
time.sleep(.5)


#wipe red then blue, then white
for i in range(disp.width):
    disp.vline(i,0,disp.height,color(255,0,0))
time.sleep(.5)
for i in range(disp.height):
    disp.hline(0,i,disp.width,color(0,0,255))
for i in range(disp.height):
    disp.hline(0,i,disp.width,color(255,255,255))

time.sleep(.5)

#place circle, rectangle, h-line, vline

disp.round_rect(20,20,30, 30, 15, color(0,0,255))

disp.rect(100,20,15,30,color(200,200,200))

disp.vline(120,0,100,color(200,200,0))
disp.hline(0,100,100,color(200,200,0))


time.sleep(3.5)


# using a rounded rectangle for such
disp.round_rect(0,0,disp.width, disp.height, 20, color(0,0,255))

time.sleep(.5)


#scrolling texttext!!!!!
disp.scroll(0,20,"Bridgekeeper:",
            background = color(0,0,220), size = 2) # optional background


disp.text(0,36,"Stop! Who approacheth the Bridge of Death must answer me these questions three, ere the other side he see.")
#auto line break when reached edge f display
#mandatory backgrounf color, defaults to black
#this does not hase a size feature yet

disp.text(0,36+(8*4),"""LANCELOT:
Ask me the questions, bridgekeeper. I am not afraid.
BRIDGEKEEPER:
What... is your name?
LANCELOT:
My name is 'Sir Lancelot of Camelot'.
BRIDGEKEEPER:
What... is your quest?
LANCELOT:
To seek the Holy Grail."""
          ,color = 0,  background = color(255,255,255))
#the 'text' method also has enter detection and breaks the line accordingly

time.sleep(7)

