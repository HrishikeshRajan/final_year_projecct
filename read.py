import Adafruit_BBIO.GPIO as GPIO   #this is for accessing the pins in beagle bone black
import time                         # this is time function used to implement delay function 
import adafruit_dht                 #this is the library of dh11 sensor

dhtDevice = adafruit_dht.DHT11(board.D18) # Initial the dht device, with data pin connected to:

while True:

    try:
        temperature =dhtDevice.temperature # to read the  value from dht11
        temperature_f = temperature_c * (9 / 5) + 32 #converting to temperature value
        humidity = dhtDevice.humidity
        print("Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(temperature_f, temperature_c, humidit)
        
    except RuntimeError as error:    #this block is used to handle the error
        print(error.args[0])         # thi  function prints what error is happended

     time.sleep(2.0) #delay function
 