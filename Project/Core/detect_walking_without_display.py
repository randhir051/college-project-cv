# USAGE
# python detect.py --images images

# import the necessary packages
from __future__ import print_function
from imutils.object_detection import non_max_suppression
from imutils import paths
import numpy as np
import imutils
import sys
import subprocess
import cv2

filename = sys.argv[1]
cap = cv2.VideoCapture(filename)

# initialize the HOG descriptor/person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

f_num=0

while(1):
	ret, frame = cap.read()
	if f_num == 0:
		sys.stdout.write(str(frame.shape[0]) + "\n")
		sys.stdout.flush()	
		# put max width
		sys.stdout.write(str(frame.shape[1]) + "\n")
		sys.stdout.flush()
	# load the image and resize it to (1) reduce detection time
	# and (2) improve detection accuracy
	# image = cv2.imread(imagePath)
	#frame = imutils.resize(frame, width=min(400, frame.shape[1]))
	# put max height	
	if frame is None:
		# print("Finished video")
		break
	
	# detect people in the image
	(rects, weights) = hog.detectMultiScale(frame, winStride=(4, 4),
		padding=(15, 15), scale=1.05)

	# draw the original bounding boxes
	for (x, y, w, h) in rects:
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

	# apply non-maxima suppression to the bounding boxes using a
	# fairly large overlap threshold to try to maintain overlapping
	# boxes that are still people
	rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
	pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)

	# draw the final bounding boxes
	i=1
	predict_str_ip = str(f_num)
	for (xA, yA, xB, yB) in pick:
		p=((xA+xB)/2, (yA+yB)/2)
		label=" person"+str(i)
		predict_str_ip += label + " " + str(p[0]) + " " + str(p[1])
		i+=1
	predict_str_ip += '\n'
	sys.stdout.write(predict_str_ip)
	sys.stdout.flush()
	# sys.stdout.flush()
	f_num+=1

cap.release()
cv2.destroyAllWindows()
