from pynput import keyboard
import subprocess
import psutil
import signal
import sys

vertical_process = None
horizontal_process = None
vertical_active = False
horizontal_active = False


def toggle_vertical():
    global vertical_process, vertical_active, horizontal_process, horizontal_active
    if horizontal_active:
        toggle_horizontal()
    if vertical_active:
        vertical_process.terminate()
        vertical_process.wait()
        vertical_process = None
        vertical_active = False
        print("Vertical restriction deactivated")
    else:
        vertical_process = subprocess.Popen(["python", "vertical_mouse.py"])
        vertical_active = True
        print("Vertical restriction activated")


def toggle_horizontal():
    global vertical_process, vertical_active, horizontal_process, horizontal_active
    if vertical_active:
        toggle_vertical()
    if horizontal_active:
        horizontal_process.terminate()
        horizontal_process.wait()
        horizontal_process = None
        horizontal_active = False
        print("Horizontal restriction deactivated")
    else:
        horizontal_process = subprocess.Popen(["python", "horizontal_mouse.py"])
        horizontal_active = True
        print("Horizontal restriction activated")


def on_press(key):
    try:
        if key.char == 'r':
            toggle_horizontal()
        elif key.char == 't':
            toggle_vertical()
    except AttributeError:
        pass


def signal_handler(sig, frame):
    global vertical_process, horizontal_process
    if vertical_process:
        vertical_process.terminate()
        vertical_process.wait()
    if horizontal_process:
        horizontal_process.terminate()
        horizontal_process.wait()
    sys.exit(0)


def main():
    signal.signal(signal.SIGINT, signal_handler)
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


if __name__ == "__main__":
    main()
