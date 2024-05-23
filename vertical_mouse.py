import time
import pyautogui
import signal
import sys

running = True


def signal_handler(sig, frame):
    global running
    running = False
    print("Stopped vertical restriction")
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)


def get_mouse_position():
    return pyautogui.position()


def set_mouse_position(x, y):
    pyautogui.moveTo(x, y, duration=0.0)


def toggle_vertical():
    global running
    running = not running
    print("Vertical restriction toggled:", running)


def main():
    initial_x, _ = get_mouse_position()
    print("Started vertical restriction")
    while running:
        x, y = get_mouse_position()
        if x != initial_x:
            set_mouse_position(initial_x, y)
        time.sleep(0.001)


if __name__ == "__main__":
    main()
