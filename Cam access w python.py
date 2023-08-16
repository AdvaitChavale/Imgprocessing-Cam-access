import cv2 #import opencv library
vs = cv2.VideoCapture(0) #initialize camera
while True: #infinite loop
	_,img = vs.read() #read the frame from camera
	cv2.imshow("VideoStream", img) #show a frame
	#3 below line, frame will show continuously until you press q button in ur keyboard
	key = cv2.waitKey(1) & 0xFF #record my key press - Hex.
	if key == ord("q"): 
		break #infinite loop will be broken
vs.release() #release the camera
cv2.destroyAllWindows() #all opened windows will be closed
