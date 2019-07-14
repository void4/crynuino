from time import time, sleep
from PIL import Image
#from mss import mss
from serial import Serial
import io

def FPSLimit(fps):
	delay = 1/fps
	current = time()
	while True:
		now = time()
		if now-current>delay:
			sleep(now-current)
			current = now
		yield

print("Opening screenshot tool")
#sct = mss()
#import pyscreenshot as ImageGrab

def screenshot(width, height):

	"""
	# Get first monitor
	monitor = sct.monitors[1]

	# Get raw pixels from the screen
	sct_img = sct.grab(monitor)

	img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
	"""
	#img = ImageGrab.grab(backend='gnome-screenshot')
	img = Image.open("image.jpg")

	img = img.resize((width, height))

	return img

ser = None
def init_serial(path, baud):
	global ser
	ser = Serial(path, baud)
	print("Connected to serial: %s" % ser.name)

def image_to_arduino(img):
	if ser is None:
		print("Call init_serial with path to Arduino first")

	# Convert to 1-bit-per-pixel black and white
	# This applies dithering by default
	blackwhite = img.convert("1")

	# Results in W*H/8 bytes, 8 pixels per byte, little endian
	bytes = img.tobytes()

	# Alternatively, to get any image format, use this:
	"""
	bytes = io.BytesIO()
	img.save(bytes, format="PNG")
	bytes = bytes.getvalue()
	"""

	ser.write(bytes)

	print("Image sent: %i bytes" % len(bytes))
