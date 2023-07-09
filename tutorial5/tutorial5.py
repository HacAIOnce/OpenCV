# color detection

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # membuat warna hsv
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # membuat warna hsv
    # [hue, saturation, value] hue=warna, saturation=kepekatan, value=kecerahan/keterangan
    lower_blue = np.array([35,25,2])
    upper_blue = np.array([92, 255, 255])


    # cv2.inRange(frame_hsv, lower collor, upper color)
    # maks menampilkan warna hitam jika tidak sesuai range warna dan warna putih jika range warna sama
    mask = cv2.inRange(hsv, lower_blue, upper_blue) # membuat mask atau lapisan

    # cv2.bitwise_and(frame1, frame2, mask)
    # 1 and 1 = 1
    # 1 and 0 = 0
    # 0 and 1 = 0
    # 0 and 0 = 0
    # maka jika frame1 dan frame 2 tidak sama maka frame akan hitam
    # jika sama maka akan sesuai dengan warna yang kita inginkan
    result = cv2.bitwise_and(frame, frame, mask=mask) 

    cv2.imshow("Camera", result)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.release()
cv2.destroyAllWindows()