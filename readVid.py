import cv2 as cv

# Read a video from a file
capture = cv.VideoCapture('Videos/dog.mp4')
# capture = cv.VideoCapture(0)

while True:
    # Read a frame from the video
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)
    
    # Check if the frame was read correctly
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

# Release the video capture object and close all OpenCV windows
capture.release()

# Close all OpenCV windows
cv.destroyAllWindows()