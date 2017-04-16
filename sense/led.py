#! /usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

red = 16
yellow = 20
green = 21

GPIO.setup(red, GPIO.OUT)
GPIO.setup(yellow, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)

GPIO.output(red, False)
GPIO.output(yellow, False)
GPIO.output(green, False)

for i in xrange(0, 100):
 GPIO.output(red, True)
 time.sleep(0.02)
 GPIO.output(green, False)

 time.sleep(0.2)

 GPIO.output(yellow, True)
 time.sleep(0.02)
 GPIO.output(red, False)

 time.sleep(0.2)
 
 GPIO.output(green, True)
 time.sleep(0.02)
 GPIO.output(yellow, False)

 time.sleep(0.2)
 print(i)

GPIO.output(red, False)
GPIO.output(yellow, False)
GPIO.output(green, False)
