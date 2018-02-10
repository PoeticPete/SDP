from gpiozero import LED
from signal import pause

pin = input("Which GPIO pin is the LED? ")

led = LED(int(pin))

led.blink()
pause()
