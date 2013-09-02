#!/usr/bin/python

import sys
import pygame
import pygame.camera
import RPi.GPIO as GPIO
import time
import uuid
from datetime import datetime, timedelta

pygame.init()
pygame.camera.init()

#create fullscreen display 640x480
#screen = pygame.display.set_mode((640,480),0)

#find, open and start low-res camera
cam_list = pygame.camera.list_cameras()
webcam = pygame.camera.Camera(cam_list[0],(64,48))
webcam.start()




PIR = 23
LED = 24
ALARM = 25

cameraEnabled = True
cameraShotTime = datetime.now()

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

    if (datetime.now() - cameraShotTime) > timedelta(seconds = 30):
	print 'camera enabled'
	print 'cameraShotTime: ' + str(cameraShotTime)
	print datetime.now()
	print datetime.now() - cameraShotTime
	cameraEnabled = True

    if (pirVal == True and cameraEnabled == True):	# check if the input is HIGH
        fireLED()	# turn LED ON
	#fire()                  # GPIO.output(ALARM,True) # Noise
	imagen = webcam.get_image();
	imagen = pygame.transform.scale(imagen,(640,480))
	pygame.image.save(imagen, '/home/pi/projects/BatchPoster/ImageDrop/' + str(uuid.uuid4()) + '.jpeg')
	cameraEnabled = False
	cameraShotTime = datetime.now()
	#screen.blit(imagen,(0,0))
        #pygame.display.flip()

	#draw all updates to display
	#pygame.display.update()
        if (pirState == False):
            # we have _just_ turned on
            pirState = True
    else:
        # GPIO.output(LED, False)	# turn LED OFF
        if (pirState == True):
            # we have _just_ turned off
            time.sleep(1)
            pirState = False;



