import numpy as np
import cv2

cap = cv2.VideoCapture("fight2.mp4")

fgbg = cv2.BackgroundSubtractorMOG()

# initialize the HOG descriptor/person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

while(1):
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    img = frame*fgmask[:,:,np.newaxis]
    cv2.imshow('frame',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()