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
# LED variables
LEDred = 18
LEDyellow = 23
LEDgreen = 24

# Buzzer variable
PINBuzzer = 26

# Switch variable
ButtonPin = 25


# set up each of the input (switch) and output (LEDs, Buzzer) pins
# LED setup
GPIO.setup(LEDred, GPIO.OUT)
GPIO.setup(LEDyellow, GPIO.OUT)
GPIO.setup(LEDgreen, GPIO.OUT)

# button output
GPIO.setup(ButtonPin, GPIO.IN) 
# buzzer output - initialized to 'off'
GPIO.setup(PINBuzzer, GPIO.OUT)
GPIO.output(PINBuzzer, GPIO.LOW)

# LED output
GPIO.output(LEDred, GPIO.LOW)
GPIO.output(LEDyellow, GPIO.LOW)
GPIO.output(LEDgreen, GPIO.LOW)

# define a function for the initial state (Green LED on, rest off)
# (if you have the second 'pedestrian LEDs, turn the red on & green off)
def StartGreen():
    # remember all code in the function is indented
    GPIO.output(LEDred, GPIO.LOW)
    GPIO.output(LEDgreen, GPIO.HIGH)
    

# Turn the green off and the amber on for 3 seconds
# ('pedestrian' red LED stays lit)
def SteadyAmber():
    # remember all code in the function is indented
    GPIO.output(LEDgreen, GPIO.LOW)
    GPIO.output(LEDyellow, GPIO.HIGH)
    time.sleep(3)

# turn the amber off, and then the red on for 1 second
def SteadyRed():
    # remember all code in the function is indented
    GPIO.output(LEDyellow, GPIO.LOW)
    GPIO.output(LEDred, GPIO.HIGH)
    time.sleep(1)

# sound the buzzer for 4 seconds
# (if you have the 'pedestrian' LEDs, turn the red off and green on)
def StartWalking():
    # make the buzzer buzz on and off, half a second of
    # sound followed by half a second of silence
    for sound_count in range(0, 10):
   		GPIO.output(PINBuzzer, GPIO.HIGH)
   		time.sleep(0.5)
   		GPIO.output(PINBuzzer, GPIO.LOW)
   		time.sleep(0.5)
   		

# turn the buzzer off and wait for 2 seconds
# (if you have a second green 'pedestrian' LED, make it flash on and
# off for the 2 seconds)
def DontWalk():
    # remember all code in the function is indented
    GPIO.output(PINBuzzer, GPIO.LOW)
    time.sleep(2)


# flash the amber on and off for 6 seconds
# (and the green 'pedestrian' LED too)
def FlashingAmberGreen():
    # remember all code in the function is indented
    for flash_amber in range(0,8):
    	GPIO.output(LEDyellow, GPIO.HIGH)
    	time.sleep(0.5)
    	GPIO.output(LEDyellow, GPIO.LOW)
    	time.sleep(0.5)


# flash the amber for 1 more second
# (turn the green 'pedestrian' LED off and the red on)
def FlashingAmber():
    # remember all code in the function is indented
    GPIO.output(LEDyellow, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(LEDyellow, GPIO.LOW)
    time.sleep(0.5)


# go throughout the traffic light sequence by calling each function
# one after the other
def TrafficLightSequence():
    # remember all code in the function is indented
    # green is already on
    SteadyAmber()
    SteadyRed()
    StartWalking()
    DontWalk()
    FlashingAmberGreen()
    FlashingAmber()
    StartGreen()
    

# sequence code starts here
    
os.system('clear') # clears the screen
print("Traffic Lights")
print("Press button to start traffic light sequence")

# initialize the traffic lights
StartGreen()


# this is the loop that waits at least 20 seconds before
# stopping the cars if the button has been pressed
while True: # loop around forever
    ButtonNotPressed = True # button has not been pressed
    start = time.time() # records the current time
    while ButtonNotPressed: # while the button has not been pressed
        time.sleep(0.1) # wait for 0.1s
        if GPIO.input(ButtonPin) == False:  # if the button is pressed
            now = time.time()
            ButtonNotPressed = False # Button has been pressed
            if (now - start) <= 20: # if under 20 seconds
                time.sleep(20 - (now - start)) # wait until 20s is up
            TrafficLightSequence() # run the traffic light sequence
GPIO.cleanup()









    



