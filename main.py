import cv2
from hand_tracking import HandDetector
from keyboard import draw_keyboard, check_key_press
from key_simulator import KeySimulator
from utils.config import KEYS


cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(detectionCon=0.8)
key_sim = KeySimulator()

typed_text = ""  # Keep the typed text here
highlighted_key = None

while True:
    success, frame = cap.read()
    frame = cv2.flip(frame, 1)

    # Draw a white rectangle on top as the text box background
    cv2.rectangle(frame, (50, 20), (1180, 100), (255, 255, 255), -1)

    # Show the typed text
    cv2.putText(frame, typed_text, (60, 80), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 3)

    hand_landmarks = detector.findHands(frame)

    # Draw keyboard and get buttons drawn
    draw_keyboard(frame, KEYS, highlighted_key)

    if hand_landmarks:
        lmList = detector.findPosition(frame, hand_landmarks[0])
        key = check_key_press(lmList, KEYS)

        if key is not None and isinstance(key, str):
            if key != highlighted_key:
                highlighted_key = key
                # Process key
                if key == "<-":
                    typed_text = typed_text[:-1]
                elif key == "Space":
                    typed_text += " "
                elif key == "Exit":
                    break
                else:
                    typed_text += key

    else:
        highlighted_key = None  # No hand detected, no highlight

    cv2.imshow("AI Virtual Keyboard", frame)

    if cv2.waitKey(1) == ord(' '):
        break

cap.release()
cv2.destroyAllWindows()
