import cv2
import os

def capture_image(output_path="user_photo.jpg"):
    # Initialize the camera (default is the first camera)
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        print("Error: Could not access the camera.")
        return

    # Read a frame from the camera
    ret, frame = camera.read()

    if ret:
        # Save the captured image to the specified path
        cv2.imwrite(output_path, frame)
        print(f"Image captured and saved as {output_path}")
    else:
        print("Error: Could not capture an image.")

    # Release the camera and close any OpenCV windows
    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_image("user_photo.jpg")




