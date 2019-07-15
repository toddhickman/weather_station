import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

GPIO.output(16, GPIO.LOW)
GPIO.output(18, GPIO.HIGH)
GPIO.output(23, GPIO.HIGH)
print("Everything's OFF.")
flag = 1

for i in range(4):
  flag = i%2
  if flag == 1:
    GPIO.output(16, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(18, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(23, GPIO.HIGH)
    print("All pins set HIGH.")
    time.sleep(3)
  else:
    GPIO.output(23, GPIO.LOW)
    time.sleep(1)
    GPIO.output(18, GPIO.LOW)
    time.sleep(1)
    GPIO.output(16, GPIO.LOW)
    print("All pins set LOW.")
    time.sleep(3)

GPIO.cleanup()
