import cv2
from hand_tracking import HandDetector
from keyboard import draw_keyboard, check_key_press
from key_simulator import KeySimulator
from utils.config import KEYS

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon = 0.8)
key_sim = KeySimulator

while True:
    success, frame = cap.read()
    frame = cv2.flip(frame, 1)
    hand_landmarks = detector.findHands(frame)

    if hand_landmarks:
        lmList = detector.findPosition(frame, hand_landmarks[0])
        draw_keyboard(frame, KEYS)
        key = check_key_press(lmList, KEYS)
        if key:
            key_sim.press(KEYS)
    else:
        draw_keyboard(frame, KEYS)


    cv2.imshow("Virtual Keyboard", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()