import cv2 as cv
# img = cv.imread("D:\Computer Vision\image\dog2.jpeg")
# cv.imshow('cat', img)
# cv.waitKey(0)

# reading video

capture = cv.VideoCapture("D:\Computer Vision\Video\dog.mp4")
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
capture.release()
cv.destroyAllWindows()
