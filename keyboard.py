from utils.button import Button
import cv2
buttons = []


def draw_keyboard(img, KEYS, highlight_key=None):
    global buttons
    buttons = []
    key_width = 60
    key_height = 60

    y_start = 120
    x_start = 100

    for i, row in enumerate(KEYS):
        x = x_start
        y = y_start + i * (key_height + 10)
        for key in row:
            w = key_width
            if key == "Space":
                w = key_width * 4
            btn = Button(x, y, w, key_height, key)
            btn.draw(img)
            buttons.append(btn)
            x += w + 10

        # Add Exit button top-right corner
    img_w = img.shape[1]
    exit_x = img_w - key_width - 30
    exit_y = 30

    exit_btn = Button(exit_x, exit_y, key_width, key_height, "Exit")
    exit_btn.draw(img)
    buttons.append(exit_btn)


def check_key_press(lmList, KEYS):
    if len(lmList) == 0:
        return None

    x8, y8 = lmList[8][1], lmList[8][2]
    x12, y12 = lmList[12][1], lmList[12][2]

    for btn in buttons:
        if btn.x < x8 < btn.x + btn.w and btn.y < y8 < btn.y + btn.h:
            # Check finger curl/press condition
            if abs(y8 - y12) < 30:
                # Highlight pressed button
                cv2.rectangle(btn.img, (btn.x, btn.y), (btn.x + btn.w, btn.y + btn.h), (0, 255, 0), -1)
                cv2.putText(btn.img, btn.text, (btn.x + 10, btn.y + 40), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 4)
                return btn.text
    return None
