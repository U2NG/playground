# RPi sense hat tests

# import sense hat software and create a 'sense' object
from sense_emu import SenseHat
sense = SenseHat()

# sense ojbject loop
while True:
    sense.show_message("Hello my name is Rembot", scroll_speed=0.05, text_colour=[255,255,0], back_colour=[0,255,255])

