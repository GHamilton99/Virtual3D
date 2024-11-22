import cv2
import numpy as np
import pygame
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from camera1 import capture_image
from camera2 import detect_face

def init_3d_environment():
    """Initialize a basic 3D environment with OpenGL."""
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Set background color to black
    glEnable(GL_DEPTH_TEST)  # Enable depth testing for 3D effects
    gluPerspective(45, 1.0, 0.1, 50.0)  # Setup perspective projection

def draw_3d_object():
    """Draw a simple 3D cube for visualization."""
    glPushMatrix()
    glRotatef(30, 1, 1, 0)  # Rotate the object for effect
    glBegin(GL_QUADS)

    # Cube vertices (a simple cube centered at origin)
    vertices = [
        [-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],
        [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1]
    ]

    # Define the faces of the cube
    faces = [
        [0, 1, 2, 3], [3, 2, 6, 7], [7, 6, 5, 4], [4, 5, 1, 0],
        [1, 5, 6, 2], [4, 0, 3, 7]
    ]

    # Draw each face
    for face in faces:
        glColor3fv((1, 0, 0))  # Set color to red
        for vertex in face:
            glVertex3fv(vertices[vertex])

    glEnd()
    glPopMatrix()

def main():
    # Initialize camera and capture photo
    capture_image("user_photo.jpg")

    # Perform face detection on the captured photo
    detect_face("user_photo.jpg")

    # Initialize pygame and OpenGL
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)

    init_3d_environment()

    # Main loop for 3D rendering
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Clear screen and depth buffer
        draw_3d_object()  # Draw a rotating cube
        pygame.display.flip()  # Update the display
        pygame.time.wait(10)  # Control the frame rate

if __name__ == "__main__":
    main()
