#!/usr/bin/python
import sys
import time
import Adafruit_DHT

while True:

    time.sleep(3)
    curr_time = time.strftime("%Y%m%d %H:%M:%S")
    humidity, temperature_c = Adafruit_DHT.read_retry(11, 2)
    temperature_f = (temperature_c * 1.8) + 32
    print '{0:} - Temp: {1:0.1f} F  Humidity: {2:0.1f} %'.format(curr_time, temperature_f, humidity)
