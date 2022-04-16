import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)

while True:
    _, img = cap.read()
    hand, img = detector.findHands(img)
    if hand:
        hand1 = hand[0]
        lmList1 = hand1["lmList"]
        bbox1 = hand1['bbox']
        fingers = detector.fingersUp(hand1)
        if fingers == [1,1,1,1,1]:
            print("Open Hand")
        elif fingers == [0,1,0,0,0]:
            print("Index")
        elif fingers == [0,0,0,0,0]:
            print("Fist")
        elif fingers == [0,0,1,0,0]:
            print("Middle")
        elif fingers == [0,1,1,0,0]:
            print("Victory")
    cv2.imshow("Image", img)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()


