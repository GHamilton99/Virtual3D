## This will be an object oriented version of the virtual3d game.
import cv2
import numpy as np

class FaceFinder:

    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

        """for (x, y, w, h) in faces:
          cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
          return ((x + w//2), y + (h//2))"""


    def find_faces(self, frame):
        '''Returns a list of center points for all detected faces.'''
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)

        if len(faces) == 0:
            return None  # No faces detected

        face_centers = []
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
            face_centers.append((x + w // 2, y + h // 2))

        return face_centers

class Stage:
    ''' Initialized with display size with display size, draws background grid based on position.'''
    def __init__(self):
        self.disp_h = 0
        self.disp_w = 0
        self.disp_h = 720
        self.disp_w = 1280
        self.disp_x = 960

    # User's position
    def draw_target_xy(self, img, pos, size):
      cv2.circle(img, pos,
                 size, (0, 0, 255), -1)
      cv2.circle(img, pos,
                 int(size*.8), (255, 255, 255), -1)
      cv2.circle(img, pos,
                 int(size*.6), (0, 0, 255), -1)
      cv2.circle(img, pos,
                 int(size*.4), (255, 255, 255), -1)
      cv2.circle(img, pos,
                 int(size*.2), (0, 0, 255), -1)


    # Draw a face-scanning target with size and position being relative
    def draw_targetz(self, pos, facexy):
      tx, ty, tz, = pos
      cv2.circle(img, (ball0x, ball0y),
               50, (255, 0, 0), -1)
      cv2.line(img, (960+ int((600-960)*.3**2), 540) , (ball0x, ball0y), (255, 0, 0), 3)

    # Update the screen
    def update(self, facexy):
      x,y = facexy
      e = .9 # smoothing constant

      x = e * x + (1-e)*self.save_x
      self.save_x = x
      img = np.zeros([1080,1920,3])
      decay = .3
      sx = sy = 0
      dx = int((x - self.cam_w/2)*2)
      for i in range(1,7):
        sx = sx + int((960-sx)*decay)
        sy = sy + int((540-sy)*decay)
        dx = int(dx * decay)
        # print (sx,sy)
        cv2.rectangle(img, (sx+dx,sy),
                      (1920-sx+dx, 1080-sy),
                     (255,255,255), 1)
        ball0x = 600+ int((x - self.cam_w/2)*2*.6)
        ball0y = 540

        cv2.line(img, (960, 0), (960, 1080),
      (ball0x, ball0y),
   (255,0,0), 3)
        self.draw_target_xy(img, (ball0x, ball0y), 35)

        ball1x = 1000+ int((x - self.cam_w/2)*2*.2)
        ball1y = 400

        cv2.line(img,
        (960+ int ((600-960)*.3**2), 540 - int((540-340)*.3**2)),
        (ball1x, ball1y),
       (255,0,0), 3)
        self.draw_target_xy(img,
                            (ball1x, ball1y),25)
        '''Iinitializes a facecascade, detects faces, finds largest, draws fact rects.'''


        ball2x = 1100+ int((x - self.cam_w/2)*2*.9)
        ball2y = 650

        cv2.line(img,
                 (960+ int((1200-960)*.3**2), 540 - int((540-650)*.3**2)),
                 (ball2x, ball2y),
                 (255,0,0),3)
        self.draw_target_xy(img, (ball2x, ball2y), 50)

        # Display the NDArray

        cv2.imshow('game', img)


### ------------------------------------------------------------------------------
ff = FaceFinder()
stage = Stage()
#img = cv2.imread('brick-walll.jpg')
img = np.zeros([1080,1920,3])
cv2.imshow('Game', img)
cap = cv2.VideoCapture(cv2.CAP_ANY)
if not cap.isOpened():
  print("Cannot open camera, make sure webcam is on")
  print("and that it's not being used by another app")
  exit()

moved = False
while True:

# Read the frame
  ret, frame = cap.read()
  if not ret:
    print("Error reading frame. Exiting ...")

facexy = ff.find_face(frame)
frame_small = cv2.resize(frame, (frame.shape[1]//4, frame.shape[0]//4), interpolation=cv2.INTER_LINEAR)
cv2.imshow('frame', frame_small)
if not moved:
  cv2.moveWindow('q to quit', 1080,0)
  moved = True
if cv2.waitKey(1) == ord('q'):

  img = stage.update(facexy)
cv2.imshow('Game', img)
# ------------------------------------------------------------------------------
ff = FaceFinder()
stage = Stage()

cap = cv2.VideoCapture(cv2.CAP_ANY)
if not cap.isOpened():
    print("Cannot open camera, make sure webcam is on")
    print("and that it's not being used by another app")
    exit()

moved = False
while True:
    # Read the frame
    ret, frame = cap.read()
    if not ret:
        print("Error reading frame. Exiting ...")
        break

    facexy = ff.find_faces(frame)
    frame_small = cv2.resize(frame, (frame.shape[1] // 4, frame.shape[0] // 4), interpolation=cv2.INTER_LINEAR)
    cv2.imshow('frame', frame_small)
    if not moved:
        cv2.moveWindow('frame', 1080, 0)
        moved = True
    if facexy is not None:
        img = stage.update(facexy)
        cv2.imshow('game', img)

    # Stop if 'q' key is pressed
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()




