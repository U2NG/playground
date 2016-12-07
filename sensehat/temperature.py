from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

def fahr(celsius):
    return((celsius/5*9)+32)


temp = fahr(sense.get_temperature())
print(temp)


