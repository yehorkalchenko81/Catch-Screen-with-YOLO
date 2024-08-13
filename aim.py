import pyautogui
from yolov5 import YOLOv5
from PIL import ImageGrab
import numpy as np

model = YOLOv5('best.pt')

def enable_ai_aim():
    screenshot = ImageGrab.grab().resize((450, 450))
    img_np = np.array(screenshot)

    screen_width, screen_height = 1920, 1080
    screen_center_x, screen_center_y = screen_width // 2, screen_height // 2

    results = model.predict(img_np)

    scale_x = screen_width / 450
    scale_y = screen_height / 450

    if results and len(results):
        boxes = results.xyxy

        closest_box = None
        min_distance = float('inf')

        for box in boxes:
            if box.numpy().size < 1:
                continue

            x1, y1, x2, y2 = box[0][:4]

            x_center = int((x1 + x2) / 2 * scale_x)
            y_center = int((y1 + y2) / 2 * scale_y)

            distance = np.sqrt((x_center - screen_center_x) ** 2 + (y_center - screen_center_y) ** 2)

            if distance < min_distance:
                min_distance = distance
                closest_box = (x_center, y_center)

        if closest_box is not None:
            x_center, y_center = closest_box
            pyautogui.moveTo(x_center, y_center)
            pyautogui.click()

