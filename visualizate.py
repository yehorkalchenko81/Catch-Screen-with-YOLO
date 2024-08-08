import mss
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import torch
from yolov5 import YOLOv5

# Ініціалізація YOLOv5
device = 'cuda' if torch.cuda.is_available() else 'cpu'
model = YOLOv5('yolov5s.pt', device=device)

# Налаштування matplotlib
plt.switch_backend('TkAgg')
fig, ax = plt.subplots()
ax.axis('off')
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
fig.canvas.mpl_connect('close_event', lambda event: plt.close(fig))

with mss.mss() as sct:
    while plt.fignum_exists(fig.number):
        # Захоплення скріншота
        screenshot = sct.grab(sct.monitors[0])
        img = Image.frombytes("RGB", (screenshot.width, screenshot.height), screenshot.rgb).resize((640, 360))

        # Перетворення зображення у формат NumPy масиву
        img_np = np.array(img)

        # Обробка зображення за допомогою YOLOv5
        results = model.predict(img_np)

        # Отримання зображення з результатами
        # Припускаємо, що render() повертає масив з формою (1, height, width, channels)
        predicted_img = results.render()[0]  # Отримати перший (і єдиний) зображення з партії

        # Відображення зображення
        ax.imshow(predicted_img)
        plt.pause(0.0001)  # Пауза для оновлення вікна
