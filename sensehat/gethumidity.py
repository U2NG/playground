# Checking the current humidty using the Sense Hat
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.clear(255, 255,255)
sense.low_light = True


on_pixel = [255, 0, 0]
off_pixel = [0, 0, 0]


while True:
    humidity = sense.get_humidity()
    humidity = round(humidity, 1)
    print(humidity)
  

    if humidity > 100:
        humidity = 100.0

    pixels = []
    on_count = int((64/100.0)*humidity)
    off_count = 64 - on_count

    pixels.extend([on_pixel] * on_count)
    pixels.extend([off_pixel] * off_count)


    sense.set_pixels(pixels)
    sleep(3)
