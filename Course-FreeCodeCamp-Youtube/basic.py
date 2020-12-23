import cv2 as cv

# reading imgs

img = cv.imread('Photos/park.jpg')

""" cv.imshow('Cat', img) """

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
""" cv.imshow('Gray',gray) """

# Blur

blur = cv.GaussianBlur(img,(7,7), cv.BORDER_DEFAULT)
cv.imshow('img', blur)

#edge cascade

canny = cv.Canny(blur,125,175)
cv.imshow('canny',canny)

#dilated image

dilated = cv.dilate(canny, (3,3), iterations=1)
cv.imshow('Dilated', dilated)

#eroding

eroded= cv.erode(dilated,(3,3), iterations=1)
cv.imshow('eroded',eroded)


#resize

resize = cv.resize(img,(500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('resized',resize)

#cropping

cropped = img[50:200,200:400]
cv.imshow('cropped',cropped)

cv.waitKey(0) 