from util import FPSLimit, screenshot, image_to_arduino

OLED_WIDTH = 128
OLED_HEIGHT = 64

FPS = 10

fpslimit = FPSLimit(FPS)

while True:
    img = screenshot(OLED_WIDTH, OLED_HEIGHT)
    image_to_arduino(img)
    next(fpslimit)

img.show()
