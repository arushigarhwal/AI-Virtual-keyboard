import cv2
class Button:
    def __init__(self, x, y, w, h, text):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.text = text
        self.img = None

    def draw(self, img):
        self.img = img
        cv2.rectangle(img, (self.x, self.y), (self.x + self.w, self.y + self.h), (255, 0, 255), -1)
        cv2.putText(img, self.text, (self.x + 15, self.y + 50), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
