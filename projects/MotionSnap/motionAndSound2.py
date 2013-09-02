import RPi.GPIO as GPIO
import time

PIR = 23
LED = 24
ALARM = 25

pirState = False	# we start, assuming no motion detected
pirVal = False	# we start, assuming no motion detected
alarmVal = False

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(ALARM, GPIO.OUT)

def delay(j):
  for k in range(1,j):
     pass

def fire():
  for j in range(1,1100):
    GPIO.output(ALARM,True)
    delay(j)
    GPIO.output(ALARM,False)
    delay(j)

def fireLED():
  for l in range(1,250):
    GPIO.output(LED,True)
    delay(l)
    GPIO.output(LED,False)
    delay(l)


while True:
    pirVal = GPIO.input(PIR)	# read input value

    if (pirVal == True):	# check if the input is HIGH
        fireLED()	# turn LED ON
	fire()                  # GPIO.output(ALARM,True) # Noise
        if (pirState == False):
            # we have _just_ turned on
            pirState = True
    else:
        # GPIO.output(LED, False)	# turn LED OFF
        if (pirState == True):
            # we have _just_ turned off
            time.sleep(1)
            pirState = False;



