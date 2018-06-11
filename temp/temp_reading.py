# Library for http requests
import requests
# Library for DHT sensor
import Adafruit_DHT
# Library for timed actions
import time

# Set wich sensor is used (DHT11 or -22) 
sensor = Adafruit_DHT.DHT22                                             # <-- !!! EDIT IF DHT11 !!!
# Set data pin the sensor is connected to the Raspberry
pin = 22                                                                # <-- !!! EDIT IF OTHER PIN IS USED !!!

# Loop for reading sensor data and publishing http request
while True:
        # reading and formating data from sensor
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        if temperature is not None:
                temp = ('{0:0.1f}'.format(temperature))
        
        # generating the http request url
        # PRTG_SERVER_ADDR:PORT/ID_TOKEN?value=
        api_url = '<PRTG_SERVER_IP>:<PORT>/<TOKEN>?value='              # <-- !!! EDIT THIS !!!
        reading = api_url + temp

        # print command for testing purpose
#       print(temp)

        # sending the http request
        response = requests.get(reading)

        # sleeptime till next iteration
        time.sleep(10)