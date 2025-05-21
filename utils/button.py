import cv2


class Button:
    def __init__(self, x, y, w, h, text):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.text = text
        self.img = None

    def draw(self, img, highlight=False):
        self.img = img
        draw_w = self.w
        color = (200, 0, 200)

        if self.text == "Space":
            draw_w = self.w
        if self.text == "Exit":
            color = (0, 0, 255)

        if highlight:
            color = (0, 255, 0)

        cv2.rectangle(img, (self.x, self.y), (self.x + draw_w, self.y + self.h), color, -1)

        font_scale = 2
        thickness = 2
        (text_width, text_height), _ = cv2.getTextSize(self.text, cv2.FONT_HERSHEY_PLAIN, font_scale, thickness)
        text_x = self.x + (draw_w - text_width) // 2
        text_y = self.y + (self.h + text_height) // 2
        cv2.putText(img, self.text, (text_x, text_y), cv2.FONT_HERSHEY_PLAIN, font_scale, (255, 255, 255), thickness)
