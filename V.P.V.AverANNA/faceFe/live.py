# This script will detect faces via your webcam.
# Tested with OpenCV3

import time
import pygame as pg
class cface :
	def __init__ (self, bool):
		self.bool = bool
	def cface (self, wanted):
		import cv2

		cap = cv2.VideoCapture(0)

		# Create the haar cascade
		cou = 0
		faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
		while(self.bool):
			# Capture frame-by-frame
			ret, frame = cap.read()

			# Our operations on the frame come here
			gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

			# Detect faces in the image
			faces = faceCascade.detectMultiScale(
				gray,
				scaleFactor=1.1,
				minNeighbors=5,
				minSize=(30, 30)
				#flags = cv2.CV_HAAR_SCALE_IMAGE
			)

			print("Found {0} faces!".format(len(faces)))

			# Draw a rectangle around the faces
			for (x, y, w, h) in faces:
				cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)


			# Display the resulting frame
			cv2.imshow('frame', frame)
			'''
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break
			'''
				
			if cv2.waitKey(1) and cou >= wanted*60:
				cv2.imwrite("face.png", frame)
				break
			pg.time.Clock().tick(60)
			cou += 1
			
		# When everything done, release the capture
		cap.release()
		cv2.destroyAllWindows()
		
		img = cv2.imread("face.png")
		print(len(faces))
		crop_imgs = [img[y:y+h, x:x+w] for x, y, w, h in img]

		cv2.imshow("cropped", crop_imgs)
		cv2.waitKey(0)
		return [(x, y, w, h) for x, y, w, h in faces]
		
cface(1).cface(1)