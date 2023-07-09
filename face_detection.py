# haar-cascade detection in OpenCv documentation

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

while True:
    _, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), [0, 255, 0], 3)

        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eye = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
        for (xe, ye, we, he) in eye:
            cv2.rectangle(roi_color, (xe, ye), (xe+we, ye+he), [255, 0, 0], 3)


    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == 27:
        break

cv2.release()
cv2.destroyAllWindows()
