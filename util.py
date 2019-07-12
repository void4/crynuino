def FPSLimit(fps):
	delay = 1/fps
	current = time()
	while True:
		now = time()
		if now-current>delay:
			sleep(now-current)
			current = now
		yield

sct = mss()

def screenshot(width, height):
    # Get first monitor
    monitor = sct.monitors[1]

    # Get raw pixels from the screen
    sct_img = sct.grab(monitor)

    img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")

    img = img.resize((width, height))

    return img
