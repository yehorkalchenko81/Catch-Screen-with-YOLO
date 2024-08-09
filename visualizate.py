import mss
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import torch
from yolov5 import YOLOv5

from getscreen import capture_screen_excluding_area

device = 'cuda' if torch.cuda.is_available() else 'cpu'
model = YOLOv5('yolov5s.pt', device=device)
model.model.classes = [0]

# Налаштування matplotlib
plt.switch_backend('TkAgg')
fig, ax = plt.subplots()
ax.axis('off')
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
fig.canvas.mpl_connect('close_event', lambda event: plt.close(fig))

with mss.mss() as sct:
    ax.imshow(np.random.random((640, 360, 3)))
    plt.pause(0.0001)  # Пауза для оновлення вікна
    while plt.fignum_exists(fig.number):
        # Захоплення скріншота
        img = capture_screen_excluding_area().resize((640, 360))

        img_np = np.array(img)

        results = model.predict(img_np)

        predicted_img = results.render()[0]

        # Відображення зображення
        ax.imshow(predicted_img)
        plt.pause(0.0001)  # Пауза для оновлення вікна
