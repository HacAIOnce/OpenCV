# laad the image

import cv2

"""
1, cv2.IMREAD_COLOR        : Loads a color image. Any transparency of image will be neglected(diabaikan). It is the default flag
0, cv2.IMREAD_GRAYSCALE    : Loads image in grayscale(skala abu-abu) mode
-1, cv2.IMREAD_UNCHANGED    : Loads image as such including alpha channel
"""
# source imread modes: https://docs.opencv.org/3.4/d8/d6a/group__imgcodecs__flags.html

img = cv2.imread('../assets/redvelvet.jpg', 1)
print(img)
# change the size
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
# img = cv2.resize(img, dsize=[0, 0], fx=0.5, fy=0.5)
"""
untuk width dan height bisa dengan (width, height) atau dsize=[widht, height]
bisa juga dengan fx dan fy, jika fx/fy = 0.5 berarti ukurannya setengah dari ukuran aslinya
kalau fx/fy = 2 maka ukurannya dua kali lipat dari ukurannya. Tetap kita harus buat width=0 dan height=0  
"""

# rotate image
img = cv2.rotate(img, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE) #akan memutar ke arah kiri sebanyak 90 derajat

# # write the image or manipulate the image
# img = imwrite('red_90vet.jpg', img)

# show the img
cv2.imshow('Redvelvet', img)

# duration show, if 0 means infinity
cv2.waitKey(0)
# destroy the windows until press any key
cv2.destroyAllWindows()