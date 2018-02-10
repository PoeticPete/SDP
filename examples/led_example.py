from gpiozero import LED
from signal import pause

print("Press ctrl+c to quit at any time")

pin = input("Which GPIO pin is the LED? ")

led = LED(int(pin))

led.blink()
pause()
