import cv2 as cv

# Read an image from a file
img = cv.imread('Photos/cat.jpg')

# Display the image in a window
cv.imshow('Cat', img)

# Wait for a key press indefinitely or for a specified amount of time
cv.waitKey(0)