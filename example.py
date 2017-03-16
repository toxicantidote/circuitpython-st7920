from machine import Pin
import st7920 

def run():

	# these are the standard hardware SPI pins
	sck =  Pin(14, mode=Pin.OUT) # labelled 5 on nodeMCU
	mosi = Pin(13, mode=Pin.OUT) # labelled 7 on nodeMCU
	miso = Pin(12, mode=Pin.OUT) # labelled 6 on nodeMCU # not connected, screen has no MISO line

	# create a software SPI using the standard pins
	screen = st7920.Screen(sck=sck, mosi=mosi, miso=miso)

	screen.plot(5, 5)
	screen.line(10, 10, 15, 15)
	screen.rect(20, 20, 25, 25)
	screen.fill_rect(30, 30, 40, 40)
	screen.fill_rect(32, 32, 38, 38, False)

	screen.redraw()
