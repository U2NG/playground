# RPi sense hat tests

# import sense hat software and create a 'sense' object
from sense_emu import SenseHat
from time import sleep
from random import randint

sense = SenseHat()


# sense ojbject
r= randint(0,255)
sense.show_letter("S", text_colour=[r,0,0])
sleep(1)

r= randint(0,255)
sense.show_letter("M", text_colour=[0,0,r])
sleep(1)

r= randint(0,255)
sense.show_letter("E", text_colour=[r,0,0])
sleep(1)

r= randint(0,255)
sense.show_letter("L", text_colour=[0,r,0])
sleep(1)

r= randint(0,255)
sense.show_letter("L", text_colour=[r,0,0])
sleep(1)

r= randint(0,255)
sense.show_letter("Y", text_colour=[0,0,0], back_colour=[255,255,255])
sleep(1)

sense.clear()
