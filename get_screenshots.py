from PIL import ImageGrab
import time

time.sleep(5)

for i in range(100):
    screenshot = ImageGrab.grab().resize((300,300))
    screenshot.save(f"dataset/screenshot{i}.png")
    time.sleep(0.1)

