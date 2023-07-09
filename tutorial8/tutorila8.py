import cv2

cap = cv2.VideoCapture(0)

# github for haarcascades : https://github.com/opencv/opencv/tree/4.x/data/haarcascades
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')


while True:
    _, frame = cap.read()

    # make gray color camera 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detect face
    # detectMultiScale(src/gray image, scaleFactor, minNeighbors)
    # scaleFactor : we shrink the image. scale factor basically create our scale pyramid.
    #               1.05 is good value and i use 1.3 here. the explanation is the small value will height accuracy but slower performing algorithm
    #               and larger value will less acuracy but faster performing algorithm. So we need to try the scaleFactor our self
    # minNeighbors : is how many candidate we need before determine that is object we want detect
    #                This parameter will affect the quality of the detected faces. Higher value results in less detections but with higher quality. 3~6 is a good value for it.
    # source : https://stackoverflow.com/questions/20801015/recommended-values-for-opencv-detectmultiscale-parameters
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), [0, 255, 0], 3)
        # make ROI(Region Of Interest) for eye detection
        roi_gray = gray[y:y+h, x:x+w] 
        roi_color = frame[y:y+h, x:x+w]
        # detect eye
        eye = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
        for (xe, ye, we, he) in eye:
           cv2.rectangle(roi_color, (xe, ye), (xe + we, ye + he), [255, 0, 0], 3)


    cv2.imshow("frame", frame)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.release()
cv2.destroyAllWindows()

