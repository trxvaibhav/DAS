#!/usr/bin/env python3
import cv2
import sys

# Initialize the USB camera (index 0 is typically the first USB camera)
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    sys.exit(1)

# Set camera properties (optional, adjust resolution if needed)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Create a named window and set it to full screen
cv2.namedWindow('Camera Feed', cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty('Camera Feed', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

try:
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Check if frame was captured successfully
        if not ret:
            print("Error: Failed to capture frame.")
            break

        # Display the frame
        cv2.imshow('Camera Feed', frame)

        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("\nProgram terminated by user.")

finally:
    # Release the camera and close windows
    cap.release()
    cv2.destroyAllWindows()
    print("Camera released and windows closed.")