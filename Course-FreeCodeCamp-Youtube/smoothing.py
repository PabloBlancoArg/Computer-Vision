import cv2 as cv
img = cv.imread('Photos/cats.jpg')

cv.imshow('Cats', img)

#averging

average = cv.blur(img, (7,7))
cv.imshow('Average blur', average)


# gaussian
gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Gaussian Blur', gauss)

# median blur
median = cv.medianBlur(img,3)
cv.imshow('Median', median)

# bilateral blur
bilateral = cv.bilateralFilter(img,5,15,15)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)