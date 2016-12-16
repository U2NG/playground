# RPi sense hat tests

# import sense hat software and create a 'sense' object
from sense_hat import SenseHat
sense = SenseHat()

sense.set_rotation(180)

# sense ojbject loop
while True:
    sense.show_message("Merry Christmas !!!", scroll_speed=0.05, text_colour=[255,0,0], back_colour=[0,0,0])


