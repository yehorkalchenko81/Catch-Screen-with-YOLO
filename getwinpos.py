import subprocess

def get_window_geometry_wmctrl(partial_name):
    try:
        # Виконання команди wmctrl для отримання списку вікон
        result = subprocess.run(['wmctrl', '-lG'], stdout=subprocess.PIPE)
        output = result.stdout.decode('utf-8')

        for line in output.splitlines():
            if partial_name in line:
                parts = line.split()
                x = int(parts[2])
                y = int(parts[3])
                width = int(parts[4])
                height = int(parts[5])

                monitor = {'left': x - 14, 'top': y - 83, 'width': width, 'height': height + 35}
                return monitor

        print(f"Вікно з частковою назвою '{partial_name}' не знайдено.")
        return None

    except Exception as e:
        print(f"Помилка: {e}")
        return None

