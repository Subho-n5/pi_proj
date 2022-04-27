#It is a simple program that makes the led at pin 10,21 to blink

from machine import Pin
from time import sleep

led1 = Pin(21, Pin.OUT)
led2 = Pin(10, Pin.OUT)
while True:
    led1.value(1)
    sleep(0.5)
    led1.value(0)
    led2.value(1)
    sleep(0.5)
    led2.value(0)
    #sleep(1)
