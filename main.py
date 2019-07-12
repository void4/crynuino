from time import time, sleep
from mss import mss
from PIL import Image

from util import FPSLimit, screenshot

OLED_WIDTH = 128
OLED_HEIGHT = 64

FPS = 10

fpslimit = FPSLimit(FPS)

while True:
    img = screenshot(OLED_WIDTH, OLED_HEIGHT)
    next(fpslimit)

img.show()
