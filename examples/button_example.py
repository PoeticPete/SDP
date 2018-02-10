from gpiozero import Button
from signal import pause


pin = input("Which GPIO pin is the button? ")

button = Button(int(pin))

def button_pressed():
	print("hi")

button.when_pressed = button_pressed

print("Try pressing the button!")

pause()
