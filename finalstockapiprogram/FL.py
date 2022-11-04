import RPi.GPIO as GPIO
from time import sleep
import multiprocessing


#led = red lights, led2 = green 
led = [14, 15, 7, 4, 5, 6, 12, 13, 16, 17]
led2 = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27]

#temporary load value for wave()
load = True
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)

#test function for determing when to start/stop wave
def isLoaded(x):
    if x == True:
        load = True
    else:
        load = False
    return wave(x)
    
#tells the leds to light up in wave pattern
def wave(x):
    while x == True:
        led2.reverse()
        for i in led2:
            GPIO.output(i, GPIO.LOW)
            sleep(0.1)
            GPIO.output(i, GPIO.HIGH)      
        for i in led:
            GPIO.output(i, GPIO.LOW)
            sleep(0.1)
            GPIO.output(i, GPIO.HIGH)
        led.reverse()
        for i in led:
            GPIO.output(i, GPIO.LOW)
            sleep(0.1)
            GPIO.output(i, GPIO.HIGH)
        led.reverse()
        led2.reverse()
        for i in led2:
            GPIO.output(i, GPIO.LOW)
            sleep(0.1)
            GPIO.output(i, GPIO.HIGH)
        wave(isLoaded(x))
    

#test function for stock rising and falling light flashes        
def highLow(x):
    if x == True:
        GPIO.output(led, GPIO.HIGH)
        sleep(0.5)
    elif x != True:
        GPIO.output(led2, GPIO.HIGH)
        sleep(0.5)
        


wave(True)
highLow(True)


    
GPIO.cleanup()
