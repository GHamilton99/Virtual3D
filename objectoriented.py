## This will be an object oriented version of the virtual3d game.
 
import cv2
import numpy as np

print('starting OO virtual3d')

class Facefinder:
	'''Use haan cascade filter to detect largest file from a frame.'''

	def -- init--(self):
		print('Facefinder initialize')
		self.fac_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

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
