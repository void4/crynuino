from util import FPSLimit, screenshot, init_serial, image_to_arduino

OLED_WIDTH = 128
OLED_HEIGHT = 64

FPS = 10

ARDUINO_PATH = "/dev/ttyACM0"#maybe USB0

fpslimit = FPSLimit(FPS)

init_serial(ARDUINO_PATH)

while True:
    img = screenshot(OLED_WIDTH, OLED_HEIGHT)
    image_to_arduino(img)
    next(fpslimit)
