import mediapipe
import cv2
import time


class Detector():
    def __init__(self, mode=False, maxHands=2, modelComplexity = 1, detectionConfidence=0.5, trackConfidence=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.modelComplexity = modelComplexity
        self.detectionConfidence = detectionConfidence
        self.trackConfidence = trackConfidence
        self.handModule = mediapipe.solutions.hands
        self.hands = self.handModule.Hands(static_image_mode=self.mode, max_num_hands=self.maxHands, min_detection_confidence=self.detectionConfidence, min_tracking_confidence=self.trackConfidence)
        self.drawing = mediapipe.solutions.drawing_utils

    def findHands(self, img, draw=True):
        imgProcess = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.output = self.hands.process(imgProcess)
        #print(output.multi_hand_landmarks)

        if self.output.multi_hand_landmarks:
            for hand in self.output.multi_hand_landmarks:
                if draw:
                    self.drawing.draw_landmarks(img, hand, self.handModule.HAND_CONNECTIONS)
        return img

    def findPosition(self, img, handNo=0, draw=True):
        lmList = []
        if self.output.multi_hand_landmarks:
            hand = self.output.multi_hand_landmarks[handNo]
            for id, lm in enumerate(hand.landmark):
                # print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                # print(id, cx, cy)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)
        return lmList

                #for id, landmark in enumerate(hand.landmark):
                    #h, w, c = img.shape
                    #cx, cy = int(landmark.x * w), int(landmark.y * h)
                    #print(id, cx, cy)
                    #if id == 0:
                        #cv2.circle(img, (cx, cy), 25, (255, 0, 0), cv2.FILLED)

def main():
    prevTime = 0
    currentTime = 0
    cap = cv2.VideoCapture(0)
    detector = Detector()
    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img)
        if len(lmList) != 0:
            print(lmList[4])

        currentTime = time.time()
        fps = 1//(currentTime-prevTime)
        prevTime = currentTime

        cv2.putText(img, str(fps), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 2)
        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
