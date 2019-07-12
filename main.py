from mss import mss
from PIL import Image

OLED_WIDTH =

# The simplest use, save a screen shot of the 1st monitor
sct = mss()

# Get first monitor
monitor = sct.monitors[1]

# Get raw pixels from the screen
sct_img = sct.grab(monitor)

img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")

#img = img.resize()

img.show()
