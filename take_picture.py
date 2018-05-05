import cv2

VideoCapture = cv2.VideoCapture()
VideoCapture.open("./challenge_video.mp4")

for i in range(29):
	ret, frame = VideoCapture.read()
ret, frame = VideoCapture.read()
cv2.imwrite("./test_images/test8.jpg", frame)