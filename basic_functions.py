import cv2 as cv

img = cv.imread('Photos/park.jpg')
cv.imshow('Park', img)

# 1. Convert to greyscale
# grey = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('Grey', grey)

# 2. Blur the image
blur = cv.GaussianBlur(img,(7,7), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

# 3. Edge Cascade
canny = cv.Canny(blur, 125,175)
cv.imshow('Canny Edges', canny)

# 4. Dilating the image
dilated = cv.dilate(canny,(7,7), iterations=3)
cv.imshow('Dilated', dilated)

# 5. Eroding the image
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('Eroded', eroded)

# 6. Resize the image
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# 7. Cropping the image
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)