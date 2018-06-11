# Providing PRTG with external sensordata via HTTP-requests

This project is used to provide sensordata from a Raspberry Pi to a PRTG Monitoring System by sending those via HTTP-Requests.
For this to work we need a working Raspberry Pi, the DHT22 / DHT11 sensor and a 4.7kOhm Resistor. A breadboard and jumperwires are useful.

The later goal will be to provide the data more costeffective by using the ESP8266 to read the sensors and make the HTTP-Requests.

## Connecting the Sensor to the Raspberry Pi

Looking at the front of the front of the sensor:

* Connect the left pin of the sensor to 3.3V on the Raspberry Pi
* Use the resistor to connect the next pin of the sensor to 3.3V on the Raspberry Pi
* Connect the same pin to the GPIO pin 22 on the Raspberry Pi
* Connect the right pin of the sensor to GND on the Raspberry Pi

## Creating the Sensor on the PRTG Server

We first need to create a http push data sensor via the PRTG webinterface, or Enterprise Console. In the device-tree you need to perform a right click on "localprobe" => "add a new device". Name the new device as you like (i.e. DC_Monitoring_pi) and proceed. Add new sensors to your device by performing a right click on it and "add new sensor".

### Sensor Configuration

* Name => Moniored value (i.e. Temperature, Humidity)
* Port => The port on wich the request will be recieved. For each monitored value a new port is needed
* Request Method => "GET"
* Identification Token => Choose your own, or leave `{__guid__}` to get a automatically generated after the sensor is setup
* Incoming Request => "Discard request" if you don´t want to store the values in a file
* No Incoming Data => Choose what to do, when no data is recieved
* Value Type => "Float"
* Scanning Interval => The script is set to send a vlaue every 10 seconds, so a scanning interval less than 10 seconds could result in disorted data. You can change this in line 32 of the reading script.

## Install Docker on the Raspbery Pi

Install using the get-docker script:

`curl -sSL https://get.docker.com | sh`

Add your user (pi) to the docker group:

`sudo usermod -aG docker pi`

Restart your Pi:

`sudo reboot now`

Start a test container:

`docker run hello-world`

Following output verifies you´ve installed Docker correctly:

`Hello from Docker!`
`This message shows that your installation appears to be working correctly [...]`

Lastly install docker-compose.

`sudo apt-get install docker-compose`

## Edit the Python scrpits to work in your environment

### hum_reading.py / temp_reading.py

You will find the scripts under `prtg-rpi-sensors/hum/` or `prtg-rpi-sensors/temp/`

Change line 9  to your sensor (DHT11 / DHT22)

`sensor = Adafruit_DHT.DHT22`

Change line 11 to your used GPIO-pin on the Raspberry Pi

`pin = 22`

Change line 22 to your PRTG magic URL

`api_url = '<PRTG_SERVER_IP>:<PORT>/<TOKEN>?value='`

## Starting the container

In the `hum` or `temp` folder:

`docker-compose up -d`

or:

`docker-compose -f <PATH_TO_COMPOSE_FILE> up -d`

## Stopping the container

In the `hum` or `temp` folder:

`docker-compose down`

or:

 `docker-compose -f <PATH_TO_COMPOSE_FILE> down`

## Further resources

The HTTP Push Data Sensor Manual:
<https://www.paessler.com/manuals/prtg/http_push_data_sensor>
The Adafruit Documentation for the DHT Sensors :
<https://learn.adafruit.com/dht/>
