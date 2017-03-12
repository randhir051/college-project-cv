# USAGE
# python detect.py --images images

# import the necessary packages
from __future__ import print_function
from imutils.object_detection import non_max_suppression
from imutils import paths
import numpy as np
import imutils
import cv2

cap = cv2.VideoCapture("walking.mp4")

# initialize the HOG descriptor/person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())


while(1):
	ret, frame = cap.read()
	# load the image and resize it to (1) reduce detection time
	# and (2) improve detection accuracy
	# image = cv2.imread(imagePath)
	frame = imutils.resize(frame, width=min(400, frame.shape[1]))
	orig = frame.copy()

	# detect people in the image
	(rects, weights) = hog.detectMultiScale(frame, winStride=(10, 10),
		padding=(8, 8), scale=1.05)

	# draw the original bounding boxes
	for (x, y, w, h) in rects:
		cv2.rectangle(orig, (x, y), (x + w, y + h), (0, 0, 255), 2)

	# apply non-maxima suppression to the bounding boxes using a
	# fairly large overlap threshold to try to maintain overlapping
	# boxes that are still people
	rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
	pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)

	# draw the final bounding boxes
	i=1
	for (xA, yA, xB, yB) in pick:
		cv2.rectangle(frame, (xA, yA), (xB, yB), (0, 255, 0), 2)
		cv2.putText(frame, "person "+str(i), ((xA+xB)/2, (yA+yB)/2), cv2.FONT_HERSHEY_PLAIN, 1.0, (0,255,0), 2);
		i+=1

	cv2.imshow('frame',frame)
	k = cv2.waitKey(1) & 0xff
	if k == 27:
		break;

cap.release()
cv2.destroyAllWindows()
