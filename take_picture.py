import cv2

VideoCapture = cv2.VideoCapture()
VideoCapture.open("./challenge_video.mp4")

ret, frame = VideoCapture.read()
cv2.imwrite("./test_images/test7.jpg", frame)