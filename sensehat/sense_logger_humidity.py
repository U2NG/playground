# Sense hat data logger - output to CSV #

# Libraries #
from sense_hat import SenseHat
from datetime import datetime
from time import sleep
from threading import Thread




# Logging settings #
TEMP_H=True
TEMP_P=False
HUMIDITY=True
PRESSURE=True



FILENAME = ""

# set number of lines to write to a file #
WRITE_FREQUENCY = 100

# sets the delay between logging #
DELAY = 300




# Functions #

# takes value in sense_data list and converts to strings (text)
# and joins together with the "," ##

def log_data():
    output_string = ",".join(str(value) for value in sense_data)
    batch_data.append(output_string)


# create list of headings that will be written to the
# file before any data ##
def file_setup(filename):
    header =["temp_h","temp_p","humidity","pressure","timestamp"]



    
    
    with open(filename, "w") as f:
              f.write(",".join(str(value) for value in header)+ "\n")
              


def get_sense_data():
    sense_data=[]

    sense_data.append(sense.get_temperature_from_humidity())
    sense_data.append(sense.get_temperature_from_pressure())
    sense_data.append(sense.get_humidity())
    sense_data.append(sense.get_pressure())

    sense_data.append(datetime.now())

    return sense_data

def timed_log():
    while True:
        log_data()
        sleep(DELAY)

# Main Program #
sense = SenseHat()

batch_data=[]

if FILENAME == "":
    filename = "SenseLog-"+str(datetime.now())+".csv"
else:
    filename = FILENAME+"-"+str(datetime.now())+".csv"

file_setup(filename)

if DELAY > 0:
    sense_data = get_sense_data()
    Thread(target= timed_log).start()

while True:
    sense_data = get_sense_data()
    
    print(sense_data)
    sleep(1)
    
    if DELAY == 300:
        log_data()

    if len(batch_data) >= WRITE_FREQUENCY:
        print("Writing to file...")
        with open(filename, "a") as f:
            for line in batch_data:
                f.write(line + "\n")
            batch_data = []
            
    

