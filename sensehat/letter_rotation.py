from sense_emu import SenseHat
from time import sleep


sense = SenseHat()

sense.show_letter("R")
angles = [0,90,180,270,0,90,180,270]
for r in angles:
    sense.set_rotation(r)
    sleep(0.5)

