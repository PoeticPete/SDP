import picamera
import time

image_name = 'new_image.jpg'

with picamera.PiCamera() as camera:
	camera.resolution = (200,200)	# adjust resolution 
	time.sleep(0.2)			# allow camera to auto focus and adjust brightness
	camera.capture(image_name)	# capture the image and save it to image_name file


