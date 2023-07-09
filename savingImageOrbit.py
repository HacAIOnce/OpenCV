import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 320)
cap.set(4, 240)

# define the codec and create VideoWrite object
# fourcc is a 4-byte code used to specify the video codec
fourcc = cv2.VideoWriter_fourcc(*'MP4V')
out = cv2.VideoWriter('vidOutput.mp4', fourcc, 20, (320, 240))
cv2.VideoWriter
while(cap.isOpened()):
	ret, frame = cap.read()
	if ret:

		# write the kflipped frame
		out.write(frame)

		cv2.imshow('frame', frame)
		key = cv2.waitKey(1)
		if key == ord('q'):
			break
		if key == ord('s'):
			cv2.imwrite('foto_from_video.jpg', frame)
			print('foto captured!')
	else:
		break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()