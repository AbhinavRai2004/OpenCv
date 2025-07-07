import cv2 as cv
import numpy as np

def transform_image(img,x,y):
    """
    Transforms the image by applying a translation matrix.
    
    Parameters:
    img (numpy.ndarray): The input image.
    x (int): The translation in the x direction.
    y (int): The translation in the y direction.
    
    Returns:
    numpy.ndarray: The transformed image.
    """
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)


# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

img = cv.imread('Photos/cat.jpg')
cv.imshow('Original', img)

transformed_img = transform_image(img,-100,100)
cv.imshow('Transformed', transformed_img)

#Rotation 
def rotate(img,angle, rotPoint=None):
    """
    Rotates the image by a specified angle around a rotation point.
    
    Parameters:
    img (numpy.ndarray): The input image.
    angle (float): The angle to rotate the image.
    rotPoint (tuple, optional): The point around which to rotate the image. If None, the center of the image is used.
    
    Returns:
    numpy.ndarray: The rotated image.
    """
    (hight, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, hight//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions = (width, hight)

    return cv.warpAffine(img,rotMat,dimensions)

rotated_img45 = rotate(img, 45)
rotated_img90 = rotate(img,90)

cv.imshow('Rotated', rotated_img90)


# Resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Flipping
flip = cv.flip(img, -1)
cv.imshow('Flip', flip)

# Cropping
cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)