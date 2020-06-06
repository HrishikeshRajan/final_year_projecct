import sys      
import time
import datetime
import board
import adafruit_dht
import gspread     #spreadsheet library

from oauth2client.service_account import ServiceAccountCredentials

DHT_TYPE = adafruit_dht.DHT11  # this implies that the type of sensor we are using dht11

DHT_PIN  = 'P8_11' # this implies that the sensor pin is connected to pin 11 of p8 section

dhtDevice = DHT_TYPE(DHT_PIN) #initializeing the connection with that pin

#GDOCS_OAUTH_JSON       = 'your SpreadsheetData-*.json file name'  :

GDOCS_SPREADSHEET_NAME = 'DHT' # this is our spread sheet name
FREQUENCY_SECONDS      = 30 # this impiles that the how much time it should wait for each connection

def login_open_sheet(oauth_key_file, spreadsheet):   # connecting to the google worksheet

    try:
        scope =  ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        credentials = ServiceAccountCredentials.from_json_keyfile_name(oauth_key_file, scope)
        gc = gspread.authorize(credentials)
        worksheet = gc.open(spreadsheet).sheet1 # pylint: disable=redefined-outer-name
        return worksheet
    except Exception as ex: # pylint: disable=bare-except, broad-except
        print('Unable to login and get spreadsheet.  Check OAuth credentials, spreadsheet name, \
        and make sure spreadsheet is shared to the client_email address in the OAuth .json file!')
        print('Google sheet login failed with error:', ex)
        sys.exit(1)

print('Logging sensor measurements to\ {0} every {1} seconds.'.format(GDOCS_SPREADSHEET_NAME, FREQUENCY_SECONDS))
print('Press Ctrl-C to quit.')
worksheet = None

while True:
                              # this is for Login if necessary.
    if worksheet is None:
        worksheet = login_open_sheet(GDOCS_OAUTH_JSON, GDOCS_SPREADSHEET_NAME)
    
     
    temp = dhtDevice.temperature  #this is to read from the sensor data
    humidity = dhtDevice.humidity
    if humidity is None or temp is None:
    time.sleep(2)
    continue
 
    print('Temperature: {0:0.1f} C'.format(temp))
    print('Humidity:    {0:0.1f} %'.format(humidity))


    try:
        worksheet.append_row((datetime.datetime.now().isoformat(), temp, humidity))
    except:                                                                        # pylint: disable=bare-except, broad-except
                                                                                   # Error appending data, most likely because credentials are stale.
                                                                                   # Null out the worksheet so a login is performed at the top of the loop.
        print('Append error, logging in again')
        worksheet = None
        time.sleep(FREQUENCY_SECONDS)
        continue
                                                                            # Wait 30 seconds before continuing
    print('Wrote a row to {0}'.format(GDOCS_SPREADSHEET_NAME))
    time.sleep(FREQUENCY_SECONDS)


