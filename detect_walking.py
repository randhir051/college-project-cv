# USAGE
# python detect.py --images images

# import the necessary packages
from __future__ import print_function
from imutils.object_detection import non_max_suppression
from imutils import paths
import numpy as np
import imutils
import cv2

cap = cv2.VideoCapture("walk.mp4")

# initialize the HOG descriptor/person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

target = open("output.txt", 'w')
target.truncate()
f_num=0
while(1):
	ret, frame = cap.read()
	# load the image and resize it to (1) reduce detection time
	# and (2) improve detection accuracy
	# image = cv2.imread(imagePath)
	#frame = imutils.resize(frame, width=min(400, frame.shape[1]))
	if frame == None:
		print("Finished video")
		break
	
	orig = frame.copy()

	# detect people in the image
	(rects, weights) = hog.detectMultiScale(frame, winStride=(4, 4),
		padding=(15, 15), scale=1.05)

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
	target.write(str(f_num))
	for (xA, yA, xB, yB) in pick:
		cv2.rectangle(frame, (xA, yA), (xB, yB), (0, 255, 0), 2)
		p=((xA+xB)/2, (yA+yB)/2)
		label=" person"+str(i)
		cv2.putText(frame, label, p, cv2.FONT_HERSHEY_PLAIN, 1.0, (0,255,0), 2);
		target.write(label + " " + str(p[0]) + " " + str(p[1]))
		i+=1
	target.write('\n')
	f_num+=1
	cv2.imshow('frame',frame)
	k = cv2.waitKey(1) & 0xff
	if k == 30:
		break;

target.close()
cap.release()
cv2.destroyAllWindows()
