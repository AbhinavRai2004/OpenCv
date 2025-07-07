import cv2 as cv

# Read an image from a file
#small img
# img = cv.imread('Photos/cat.jpg')

# large img
larImg = cv.imread('Photos/cat_large.jpg')

# Display the image in a window
cv.imshow('Cat', larImg)  

# Wait for a key press indefinitely or for a specified amount of time
cv.waitKey(0)