# menaruh logo ke gambar

import numpy as np
import cv2

# laod two image
img1 = cv2.imread('assets/redvelvet.jpg')
img2 = cv2.imread('assets/logo.png')

# i want to put logo op top-left corner, so i create a ROI(dalam bisnis kepanjangannya Return on Investment)
row, col, channels = img2.shape

# meposisikan logo yang kita ingin taruh. ps: width dan height nya harus sesuai dengan ukuran gambar logo / img2
roi = img1[0:row, 0:col] #posisi logo dari 0 sampai 500 karena ukuran img2 500x500
# roi = img1[100:600, 100:600] #posisi logo dari 100 sampai 600

# create mask of logo and create its inverse mask also
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY) #membuat warna img2 jadi abu-abu
# cv2.threshold(src(GrayScaleImg), threshould value, maximum value, ThreshouldType) ps: threshould value adalah ambang nilai dari kecerahan yang mau kita ambil
# source: https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html
ret, mask = cv2.threshold(img2gray, 40, 255, cv2.THRESH_BINARY) #membuat threshold untuk memisahkan object dengan backgroundnya dengan perbedaan gelap terangnya
mask_inv = cv2.bitwise_not(mask) # inverse / kebalikan dari mask

# black-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi, roi, mask = mask_inv)

# take only region of logo from logo image
img2_fg = cv2.bitwise_and(img2, img2, mask = mask)


# put logo in ROI and modify the main image
dst = cv2.add(img1_bg, img2_fg)
#menaruh dst / gabungan dari img1_bg dan img2_fg ke posisi yang sama dengan roi
img1[0:row, 0:col] = dst # menaruh keposisi width = 0 - 500 dan height = 0 -500
# img1[100:600, 100:600] = dst #menaruh keposisi width = 100-600 dan height = 100-600

cv2.imshow('hasil', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()