# camera and videocapture

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# # cek kalau kamera lagi digunakan
# if cap.isOpened():
#     print('Cannot open camera')
#     exit()

while True:
    # capture frame-by-frame
    # ret untuk mengecek apakah kamera sedang digunakan jika digunakan akan bernilai False kalau tidak akan bernilai True
    ret, frame = cap.read() 

    # get width and height
    # 3 and 4 is properti for width and height
    # dibuat integer karena cap.get() menghasilkan float dan kita tidak bisa pakai float buat frame
    # source: https://docs.opencv.org/3.4/d4/d15/group__videoio__flags__base.html#gaeb8dd9c89c10a5c63c139bf7c4f5704d
    width = int(cap.get(3))
    height = int(cap.get(4))


    # # kalau frame  terbaca dengan benar maka ret = True
    # if not ret:
    #     print("Can't receive frame")
    #     break

    # # make frame color gray
    # gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY) # source: https://docs.opencv.org/3.4/d8/d01/group__imgproc__color__conversions.html


    # make 4 frame
    image = np.zeros(frame.shape, np.uint8) # membuat frame hitam dengan numpy.zeros
    img = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5) # membuat ukuran frame menjadi seperempat
    # menaruh gambar 
    image[:height//2, :width//2] = cv2.rotate(img, cv2.cv2.ROTATE_180) # bagian atas kiri
    image[height//2:, :width//2] = img # bagian bawah kiri
    image[:height//2, width//2:] = cv2.rotate(img, cv2.cv2.ROTATE_180) # bagian atas kanan
    image[height//2:, width//2:] = img #bagian bawah kanan

    cv2.imshow('frame', image)
    if cv2.waitKey(1) == ord('q'): # make frame loop everi one miliseconds until we press q
        break                      # ord() adalah ordinal pada table ASCII

cv2.release() # melepaskan kamera dari cap
cv2.destroyAllWindows()