#!/usr/bin/python
import time
import RPi.GPIO as GPIO


# Use board based pin numbering
GPIO.setmode(GPIO.BCM)

sensor = 4
red = 26
yellow = 19

GPIO.setup(sensor, GPIO.IN)
GPIO.setup(red, GPIO.OUT)
GPIO.output(red, False)
GPIO.setup(yellow, GPIO.OUT)
GPIO.output(yellow, False)

def ReadSensor():
   return GPIO.input(sensor)

e = 0
def HandleEvent(channel):
      global e
      value = ReadSensor()
      # print e, ": Value is ", value
      e+=1
      if value==0:
         print e, ". Off"
         GPIO.output(red, 1)
         GPIO.output(yellow, 0)
      elif value==1:
         print e, ". On"
         GPIO.output(red, 0)
         GPIO.output(yellow, 1)
      else:
         print e, ". ERROR"
         GPIO.output(red, 1)
         GPIO.output(yellow, 1)



GPIO.add_event_detect(sensor, GPIO.BOTH, HandleEvent, bouncetime=10)

HandleEvent(sensor)

try:
   while True:
      pass
finally:
   GPIO.cleanup()

