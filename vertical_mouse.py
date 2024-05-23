# vertical_mouse.py
import time
import Quartz.CoreGraphics as CG
import signal
import sys

running = True


def signal_handler(sig, frame):
    global running
    running = False
    print("Stopped vertical restriction")
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


def get_mouse_position():
    event = CG.CGEventCreate(None)
    location = CG.CGEventGetLocation(event)
    return (location.x, location.y)


def set_mouse_position(x, y):
    event = CG.CGEventCreateMouseEvent(
        None, CG.kCGEventMouseMoved, (x, y), CG.kCGMouseButtonLeft)
    CG.CGEventPost(CG.kCGHIDEventTap, event)


def main():
    initial_x, _ = get_mouse_position()
    print("Started vertical restriction")
    while running:
        x, y = get_mouse_position()
        if x != initial_x:
            set_mouse_position(initial_x, y)
        time.sleep(0.01)


if __name__ == "__main__":
    main()
