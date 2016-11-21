# Traffic Light Simulator
# camjam edukit traffic lights worksheet

# import libraries
import os
import time
import RPi.GPIO as GPIO

# set the GPIO pin naming mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# set up variables for the LED, Buzzer and switch pins





# set up each of the input (switch) and output (LEDs, Buzzer) pins





# define a function for the initial state (Green LED on, rest off)
# (if you have the second 'pedestrian LEDs, turn the red on & green off)
def StartGreen():
    # remember all code in the function is indented




    

# Turn the green off and the amber on for 3 seconds
# ('pedestrian' red LED stays lit)
def SteadyAmber():
    # remember all code in the function is indented






# turn the amber off, and then the red on for 1 second
def SteadyRed():
    # remember all code in the function is indented








# sound the buzzer for 4 seconds
# (if you have the 'pedestrian' LEDs, turn the red off and green on)
def StartWalking():
    # make the buzzer buzz on and off, half a second of
    # sound followed by half a second of silence






# turn the buzzer off and wait for 2 seconds
# (if you have a second gree 'pedestrian' LED, make it flash on and
# off for the 2 seconds)
def DontWalk():
    # remember all code in the function is indented




# flash the amber on and off for 6 seconds
# (and the green 'pedestrian' LED too)
def FlashingAmberGreen():
    # remember all code in the function is indented





# flash the amber for 1 more second
# (turn the green 'pedestrian' LED off and the red on)
def FlashingAmber():
    # remember all code in the function is indented







# go throughout the traffic light sequence by calling each function
# one after the other
def TrafficLightSequence():
    # remember all code in the function is indented








os.system('clear') # clears the screen
print("Traffic Lights")

# initialize the traffic lights
StartGreen()



# this is the loop that waits at least 20 seconds before
# stopping the cars if the button has been pressed
while True: # loop around forever
    ButtonNotPressed = True # button has not been pressed
    start = time.time() # records the current time
    while ButtonNotPressed: # while the button has not been pressed
        time.sleep(0.1) # wait for 0.1s
        if GPIO.input(PinButton) == False:  # if the button is pressed
            now = time.time()
            ButtonNotPressed = False # Button has been pressed
            if (now - start) <= 20: # if under 20 seconds
                time.sleep(20 - (now - start)) # wait until 20s is up
            TrafficLightSequence() # run the traffic light sequence
GPIO.cleanup()









    



