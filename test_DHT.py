import time
import board
import adafruit_dht
 
# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT11(board.D21)
 
while True:
    try:
        # Print the values to the serial port
        temp_c = dhtDevice.temperature
        temp_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        print("Temp: {:.1f}* F,    Humidity: {}% "
              .format(temp_f, humidity))
 
    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
 
    time.sleep(2.0)
