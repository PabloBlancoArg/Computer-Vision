import cv2 as cv
import numpy as np

# reading imgs

img = cv.imread('Photos/park.jpg')

cv.imshow('park', img)

#translation

def translate(img,x,y):
    transmat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img,transmat,dimensions)

transalated = translate(img,100,100)
cv.imshow('Translate', transalated)


# rotation

def rotate(img,angle,rotPoint=None):
    (heigth,width) = img.shape[:2]
    
    if rotPoint is None:
        rotPoint = (width//2,heigth//2)

    rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions = (img.shape[1],img.shape[0])
    
    return cv.warpAffine(img,rotMat,dimensions)

rotated = rotate(img,90)
cv.imshow('rotated',rotated)

rotated_rotated = rotate(img,-90)
cv.imshow('rotated2', rotated_rotated)

# resizing

resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)


#flipping 

flip = cv.flip(img,0)
cv.imshow('Flip',flip)

#cropped

cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)