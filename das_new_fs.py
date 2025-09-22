#!/usr/bin/env python3
import cv2
import sys

# GStreamer pipeline for MJPEG capture with appsink
gst_pipeline = (
    "v4l2src device=/dev/video0 ! "
    "video/x-raw,format=UYVY,width=640,height=480,framerate=30/1 ! "
    "videoconvert ! video/x-raw,format=BGR ! appsink"
)

# Initialize the pipeline
cap = cv2.VideoCapture(gst_pipeline, cv2.CAP_GSTREAMER)

# Check if the pipeline opened successfully
if not cap.isOpened():
    print("Error: Could not open pipeline.")
    sys.exit(1)

# Target display resolution (your monitor)
DISPLAY_WIDTH, DISPLAY_HEIGHT = 1280, 720

# Create a named window and set it to full screen
cv2.namedWindow('Camera Feed', cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty('Camera Feed', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture frame.")
            break

        # Resize captured frame to display resolution
        frame_resized = cv2.resize(frame, (DISPLAY_WIDTH, DISPLAY_HEIGHT), interpolation=cv2.INTER_LINEAR)

        # Show fullscreen
        cv2.imshow('Camera Feed', frame_resized)

        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("\nProgram terminated by user.")

finally:
    cap.release()
    cv2.destroyAllWindows()
    print("Pipeline released.")
