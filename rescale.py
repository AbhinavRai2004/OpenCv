import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    # this function is work with images, videos and live video.
    """
    Rescale the given frame by a specified scale factor.

    Parameters:
    frame (numpy.ndarray): The input frame to be rescaled.
    scale (float): The scale factor for resizing the frame. Default is 0.75.

    Returns:
    numpy.ndarray: The rescaled frame.
    """
    width = int(frame.shape[1] * scale)
    hight = int(frame.shape[0] * scale)
    dimensions = (width, hight)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    # work with live video capture.

    """
    Change the resolution of the video capture to the specified width and height.

    Parameters:
    width (int): The desired width of the video capture.
    height (int): The desired height of the video capture.
    """
    capture.set(3, width)  # Set width
    capture.set(4, height)  # Set height

img = cv.imread('Photos/cat_large.jpg')
rescaled_img = rescaleFrame(img,scale=0.3)

cv.imshow('Cat Rescaled', rescaled_img)

cv.waitKey(0)

capture = cv.VideoCapture('Videos/dog.mp4')
# capture = cv.VideoCapture(0)

while True:
    # Read a frame from the video
    isTrue, frame = capture.read()
    frame_rescaled = rescaleFrame(frame)  # Rescale the frame.

    cv.imshow('Video', frame)
    cv.imshow('Video Rescaled', frame_rescaled)
    
    # Check if the frame was read correctly
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

# Release the video capture object and close all OpenCV windows
capture.release()

# Close all OpenCV windows
cv.destroyAllWindows()