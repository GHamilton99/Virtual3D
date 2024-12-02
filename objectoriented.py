## This will be an object oriented version of the virtual3d game.

import cv2
import numpy as np


print('starting OO virtual3d')

class Tunnel:
	pass


class Facefinder:
	'''Use haan cascade filter to detect largest file from a frame.'''

 	def__init__(self):
		print('Facefinder initialize')
		self.fac_cascade = 
     cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

	def find_face(self, frame):
		if faces is None:

			bx = by = bw = bh = 0

		for (x, y, w, h) in faces:
			if w > bw:
			bx., by, bw, bh = x, y, w, h

		cv2.rectangle(gray, (bx,by), (bx+bw), 
		#----------------------------------------------------
		# main
		#

		ff = Facefinder()
		print('virtual3d complete')
	def find_face(self,frame):
		""" Returns face center(x,y), draws rect on frame """

		# convert to grayscale
		gray = cv2.cvtcolor(frame,cv2.BGRZGRAY)
		faces = self.face_cascade.detectmultiscale(gray,minNeighbors = 9)
		

		faces = self.face_cascade
		# Draw rectangle 
		if faces is None:
			return None
			bx=by=bw=bh = x,y,w,h

			for (x,y,w,h) in faces 
				if w>bw: # is current face bigger than biggest found so far

			cv2.rectangle = (frame, (los,by).....3)

'''--------------------------------------------------------------------------'''
## main code
ff = facefinder()
# create cam
cap = cv2.Videocapture(cv2.cap_ANY)
if not cap.isOpened():
	print("Couldn't open cam")
	exit()

While True:
	retval, frame = cap.read()
	if retval == False:
	print("camera error!")

	ff.find_face(frame)
	cv2.imshow('q to quit', frame)

	if cv2.waitKey(30) == ord('q')



pause = input('press enter to end')

cap.release()
print('starting oo virtual3d')




