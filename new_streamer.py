#!/usr/bin/env python3
import cv2
import sys

# GStreamer pipeline for MJPEG capture with appsink
gst_pipeline = (
    "v4l2src device=/dev/video0 ! "
    "video/x-raw,format=UYVY,width=1280,height=720,framerate=30/1 ! "
    "videoconvert ! video/x-raw,format=BGR ! appsink"
)


# Initialize the pipeline
cap = cv2.VideoCapture(gst_pipeline, cv2.CAP_GSTREAMER)

# Check if the pipeline opened successfully
if not cap.isOpened():
    print("Error: Could not open pipeline.")
    sys.exit(1)

# Create a named window and set it to full screen
cv2.namedWindow('Camera Feed', cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty('Camera Feed', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

try:
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture frame.")
            break

        # Display the frame using OpenCV
        cv2.imshow('Camera Feed', frame)

        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("\nProgram terminated by user.")

finally:
    # Release the pipeline and close windows
    cap.release()
    cv2.destroyAllWindows()
    print("Pipeline released.")