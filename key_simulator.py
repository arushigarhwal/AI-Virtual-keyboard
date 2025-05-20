import time

from pynput.keyboard import Controller


class KeySimulator:
    def __init__(self):
        self.keyboard = Controller()
        self.last_pressed = ""
        self.last_time = time.time()

    def press(self, key):
        if time.time() - self.last_time > 0.3 or self.last_pressed != key:
            self.keyboard.press(key.lower())
            self.keyboard.release(key.lower())
            self.last_time = time.time()
            self.last_pressed = key
