import mss
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import torch
from yolov5 import YOLOv5

device = 'cuda' if torch.cuda.is_available() else 'cpu'
model = YOLOv5('best.pt', device=device)

plt.switch_backend('TkAgg')
fig, ax = plt.subplots()
ax.axis('off')
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
fig.canvas.mpl_connect('close_event', lambda event: plt.close(fig))

with mss.mss() as sct:
    while plt.fignum_exists(fig.number):
        monitor = sct.monitors[1]
        screenshot = sct.grab(monitor)

        img = Image.frombytes("RGB", screenshot.size, screenshot.rgb)

        img_np = np.array(img)

        results = model.predict(img_np)

        predicted_img = results.render()[0]

        ax.imshow(predicted_img)
        plt.pause(0.0001)
