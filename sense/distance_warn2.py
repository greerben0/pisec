#!/usr/bin/python
import time
import RPi.GPIO as GPIO


# Use board based pin numbering
GPIO.setmode(GPIO.BCM)

trigger = 5
echo = 6
red = 16
yellow = 20
green = 21

redDistance = 100
yellowDistance = 150

def ReadDistance():
   GPIO.setup(trigger, GPIO.OUT)
   GPIO.output(trigger, 0)

   time.sleep(0.000002)


   #send trigger signal
   GPIO.output(trigger, 1)


   time.sleep(0.01)


   GPIO.output(trigger, 0)


   GPIO.setup(echo, GPIO.IN)


   while GPIO.input(echo)==0:
      starttime=time.time()


   while GPIO.input(echo)==1:
      endtime=time.time()
      
   duration=endtime-starttime
   # Distance is defined as time/2 (there and back) * speed of sound 34000 cm/s 
   distance=duration*34000/2
   return distance


GPIO.setup(red, GPIO.OUT)
GPIO.output(red, False)
GPIO.setup(yellow, GPIO.OUT)
GPIO.output(yellow, False)
GPIO.setup(green, GPIO.OUT)
GPIO.output(green, True)

try:
   while True:
      distance = ReadDistance()
      print "Distance to object is ",distance," cm or ",distance*.3937, " inches"
      if distance < redDistance:
          GPIO.output(red, 1)
          GPIO.output(yellow, 0)
          GPIO.output(green, 0)
      elif distance < yellowDistance:
          GPIO.output(red, 0)
          GPIO.output(yellow, 1)
          GPIO.output(green, 0)
      else:
          GPIO.output(green, 1)
          GPIO.output(red, 0)
          GPIO.output(yellow, 0)
      time.sleep(.5)
finally:
   GPIO.cleanup()

