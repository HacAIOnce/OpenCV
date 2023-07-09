# Template Matching (object detection)

import cv2
from cv2 import imread
from cv2 import minMaxLoc

# image
img = cv2.resize(imread('assets/soccer_practice.jpg', 1), (0, 0), fx=0.7, fy=0.7)
# karena untuk deteksi gambar kita memerlukan warna abu-abu
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# template / image object yang dicari
template = cv2.resize(imread('assets/shoe.png', 0), (0, 0), fx=0.7, fy=0.7)

# get height=row and width=col
h, w = template.shape

# All the 6 methods for comparison in a list
methods = [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED, cv2.TM_CCOEFF, 
            cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED]

# kita perlu mencoba semua methods saat memulai template matching agar tau mana yang lebih baik untuk kita gunakan
for method in methods:
    # agar setiap perulangan img_bgr dan gray(img_gray) akan merefresh 
    # dan agar kotak untuk deteksi object tidak lebih dari satu / tidak muncul banyak
    img_bgr = img.copy() # image bgr
    gray = img_gray.copy() # img gray

    # cv2.matchTemplate(src/img, template/object, method)
    result = cv2.matchTemplate(img_gray, template, method)
    # minMaxLoc(matchTemplate) => menghasilkan min_val, max_val, min_loc, max_loc
    min_val, max_val, min_loc, max_loc = minMaxLoc(result)

    # if cv2.TM_SQDIFF dan cv2.TM_SQDIFF_NORMED, take minimum
    # if not take maximum 
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc


    bottom_right = (location[0] + w, location[1] + h)
    cv2.rectangle(img_bgr, location, bottom_right, [0, 255, 0], 2)

    cv2.imshow('image', img_bgr)

    cv2.waitKey(0)
    cv2.destroyAllWindows()