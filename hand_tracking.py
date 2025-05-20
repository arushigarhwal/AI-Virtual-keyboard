import cv2
import mediapipe as mp


class HandDetector:
    def __init__(self, detectionCon=0.5):
        self.hands = mp.solutions.hands.Hands(max_num_hands=1, min_detection_confidence=detectionCon)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                self.mpDraw.draw_landmarks(img, handLms, mp.solutions.hands.HAND_CONNECTIONS)
            return self.results.multi_hand_landmarks
        return []

    def findPosition(self, img, handLms):
        h, w, _ = img.shape
        lmList = []
        for id, lm in enumerate(handLms.landmark):
            cx, cy = int(lm.x * w), int(lm.y * h)
            lmList.append((id, cx, cy))
        return lmList

