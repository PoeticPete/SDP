import RPi.GPIO as gpio
import time

def init():
    '''
    Setup Raspberry Pi GPIO pins.
    
    '''
    
    gpio.setmode(gpio.BCM)
    gpio.setup(17, gpio.OUT) # use pin 17
    gpio.setup(22, gpio.OUT) # use pin 22
    
def move(seconds):
    '''
    moves the motor
    
    :param seconds: the number of seconds to move
    '''
    
    init()
    
    # reverse True and False to move the motor the other way
    gpio.output(17, False)
    gpio.output(22, True)
    
    time.sleep(seconds)
    gpio.cleanup()
    
move(1) # moves the motor 1 second