import cv2 as cv

# reading imgs

img = cv.imread('Photos/cat.jpg')

cv.imshow('Cat', img)

def rescaleFrame(frame, scale=0.75):
    #img,video,live
    
    width = int(frame.shape[1]*scale)
    heigth = int(frame.shape[0]*scale)

    dimensions = (width,heigth)

    return cv.resize(frame, dimensions,interpolation=cv.INTER_AREA)


resized_image= rescaleFrame(img)
cv.imshow('Image',resized_image)

def changeRes(width,height):
    #live_video
    capture.set(3,width)
    capture.set(4,height)



capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)
    cv.imshow('Video',frame)
    cv.imshow('resized Video',frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
