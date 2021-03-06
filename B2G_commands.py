
import serial   # this library used to communicate in serial
import Adafruit_BBIO.UART as UART  #to acces serial ports
from time import sleep           # used for delay 

UART.setup("UART1") # this set is activating the pin name UART1 which has tx and rx

ser=serial.Serial('/dev/ttyO1',9600)  # now we need to activate connection btw our board and gps module

class GPS: # class
   def __init__(self): # this function call when you create object
        #This sets up variables for useful commands.
        
        #This set is used to set the rate the GPS reports to our board 
        # we can selcet any one at a time
        UPDATE_10_sec=  "$PMTK220,10000*2F\r\n" #Update Every 10 Seconds
        UPDATE_5_sec=  "$PMTK220,5000*1B\r\n"   #Update Every 5 Seconds  
        UPDATE_1_sec=  "$PMTK220,1000*1F\r\n"   #Update Every One Second
        UPDATE_200_msec=  "$PMTK220,200*2C\r\n" #Update Every 200 Milliseconds

        #This set is used to set the rate the GPS takes measurements,we can selcet any one at a time
        MEAS_10_sec = "$PMTK300,10000,0,0,0,0*2C\r\n" #Measure every 10 seconds
        MEAS_5_sec = "$PMTK300,5000,0,0,0,0*18\r\n"   #Measure every 5 seconds
        MEAS_1_sec = "$PMTK300,1000,0,0,0,0*1C\r\n"   #Measure once a second
        MEAS_200_msec= "$PMTK300,200,0,0,0,0*2F\r\n"  #Meaure 5 times a second

        #Set the Baud Rate of GPS we can selcet any one at a time
        BAUD_57600 = "$PMTK251,57600*2C\r\n"          #Set Baud Rate at 57600
        BAUD_9600 ="$PMTK251,9600*17\r\n"             #Set 9600 Baud Rate

        #Commands for which NMEA Sentences are sent
        #if you want to change the board rate do uncomment the down one
        #ser.write(BAUD_57600)
        #ser.write(57600)
        #we can selcet any one at a time
        GPRMC_ONLY= "$PMTK314,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0*29\r\n" #Send only the GPRMC Sentence
        GPRMC_GPGGA="$PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0*28\r\n"#Send GPRMC AND GPGGA Sentences
        SEND_ALL ="$PMTK314,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0*28\r\n" #Send All Sentences
        SEND_NOTHING="$PMTK314,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0*28\r\n" #Send Nothing
        # this is the part of giving commands to gps from our board
        ser.write(UPDATE_1_sec)  # this fucntion does the sending of data from gps to board every 1 sec 
        sleep(1)
        ser.write(MEAS_1_sec) # this function does the measuring of gps sensor in every 1 sec
        sleep(1)
        ser.write(GPRMC_ONLY) # here we can select the variables from NMEA sets
        sleep(1)
        ser.flushInput()
        ser.flushInput()
        print ("Initializing....")

#create a object for class GPS
myGPS =GPS()
while (1): #infinte loop for continous reading
    ser.flushInput() # it clear the input buffer to avoid the data overwrite and serial monitor clean
    ser.flushInput()
    while ser.inWaiting()==0:  # if no data then do nothing and this function will be in loop until data comes
        pass

    NMEA=ser.readline()
    print (NMEA)

    #if your using GPRMC_GPGGA
    #then use two variables 
    #NMEA1=ser.readline()
    #NMEA2=ser.readline()

