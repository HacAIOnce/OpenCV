# corner detection
# source : https://opencv24-python-tutorials.readthedocs.io/en/latest/py_tutorials/py_feature2d/py_shi_tomasi/py_shi_tomasi.html

import numpy as np
import random
import cv2


img = cv2.imread('assets/chessboard.png')
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)

# membuat img menjadi gray color
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# track the corner
# cv2.goodFeaturesToTrack(img(gray color), jumlah corner yang ingin dicari, quality level / kualitas dari corner, minimum euclidean distance)
# euclidean distance adalah jika corner agak bulat dan computer akan menghitungnya 5 atau 10 atau lebih maka dari itu kita tentukan minimum euclidean distance
corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
# make corners integer
corners = np.int0(corners)


for corner in corners:
    x, y = corner.ravel() # ravel() mengubah np array [[[1,2]]] menjadi [1,2] atau [[1,2,3], [2,1]] menjadi [1,2,3,2,1]
    # membuat titik untuk setiap corner
    cv2.circle(img, (x,y), 5, [255,0,0], -1)


# drawing line to between corners
for i in range(len(corners)):
    for j in range(i+1, len(corners)):
        # take corner1 and corner2
        corner1 = tuple(corners[i][0])
        corner2 = tuple(corners[j][0])


        # color for line
        color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3)))
        
        # draw line to connect every corner
        # cara1 
        cv2.line(img, corner1, corner2, color, 1)

        # # cara2
        # cv2.line(img, corner1, corner2, [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)], 1)



cv2.imshow('Chess', img)
cv2.waitKey(0)
cv2.destroyAllWindows()