# sparkles sense hat
from sense_emu import SenseHat
from random import randint
from time import sleep



sense = SenseHat()

while True:
    x = randint(0,7)
    y = randint(0,7)

    r = randint(100,255)
    g = randint(100,255)
    b = randint(100,255)

    sense.set_pixel(x,y,r,g,b)

    
    sleep(0.01)
