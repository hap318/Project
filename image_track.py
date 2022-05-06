import cv2 as cv
import imutils
import numpy as np

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

def getColorMask(frame):
    lowerBound = np.array([0, 100, 150])
    upperBound = np.array([10, 255, 255])

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    return cv.inRange(hsv, lowerBound, upperBound)

while True:
    ret, frame = cap.read()
    frame = imutils.resize(frame, width=600)
    original = frame.copy()



    cnts = cv.findContours(getColorMask(frame), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]

    for c in cnts:
        x, y, w, h = cv.boundingRect(c)
        cv.rectangle(original, (x, y), (x + w, y + h), (36, 255, 12), 2)

    cv.imshow("back and white", getColorMask(frame))
    cv.imshow('image', original)
    if cv.waitKey(1) == ord('q'):
        break


# When everything done, release the capture
cap.release()
cv.destroyAllWindows()