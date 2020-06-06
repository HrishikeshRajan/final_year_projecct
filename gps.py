import  serial     # this library used to communicate in serial
import Adafruit_BBIO.UART as UART #to acces serial ports

UART.setup("UART1") # this set is activating the pin name UART1 which has tx and rx
 
 # now we need to activate connection btw our board and gps module
GPS=serial.Serial('/dev/ttyO1',9600)

while(1):
    while GPS.inWaiting ()==0: # it waits for data....if no data comes from gps it does nothingbut if data comes it send to board   
        pass
    NMEA=GPS.readline() #this fucntion reads all NMEA values (google about NMEA )
    print (NMEA)


