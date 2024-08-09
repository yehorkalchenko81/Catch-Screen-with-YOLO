from getwinpos import get_window_geometry_wmctrl

import mss
import mss.tools
from PIL import Image

def capture_screen_excluding_area():
    exclude = get_window_geometry_wmctrl('Figure 1')

    # Захоплення скріншоту всього екрану
    with mss.mss() as sct:
        monitor = sct.monitors[1]  # Захоплення першого монітора
        screenshot = sct.grab(monitor)

        # Конвертуємо скріншот в формат Pillow Image
        img = Image.frombytes("RGB", screenshot.size, screenshot.rgb)

        # Використання чорного кольору для заміни області
        black_area = Image.new("RGB", (exclude['width'], exclude['height']), (0, 0, 0))

        # Вставка чорного прямокутника в область, яку треба виключити
        img.paste(black_area, (exclude['left'], exclude['top']))

        # Збереження результату
        return img

