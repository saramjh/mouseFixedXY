from pynput import keyboard
import subprocess

vertical_active = False
horizontal_active = False


def toggle_vertical():
    global vertical_active, horizontal_active
    if horizontal_active:
        horizontal_active = False
        subprocess.Popen(["pkill", "-f", "horizontal_mouse.py"])
    vertical_active = not vertical_active
    if vertical_active:
        subprocess.Popen(["python", "vertical_mouse.py"])
    else:
        subprocess.Popen(["pkill", "-f", "vertical_mouse.py"])


def toggle_horizontal():
    global horizontal_active, vertical_active
    if vertical_active:
        vertical_active = False
        subprocess.Popen(["pkill", "-f", "vertical_mouse.py"])
    horizontal_active = not horizontal_active
    if horizontal_active:
        subprocess.Popen(["python", "horizontal_mouse.py"])
    else:
        subprocess.Popen(["pkill", "-f", "horizontal_mouse.py"])


def on_press(key):
    # 키 수정하는 부분
    try:
        if key.char == 'r':
            toggle_horizontal()
        elif key.char == 't':
            toggle_vertical()
    except AttributeError:
        pass


def main():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


if __name__ == "__main__":
    main()
