import cv2
import random

img = cv2.imread('assets/redvelvet.jpg', -1)

# # if we print the image on open cv it will give us a numpy of the color BGR
# print(img)
# print(img.shape[1]) #it will give us (row, column, channel)


# # change the pixel on image
# for i in range(100,500): #row from 100 to 500
#     for j in range(img.shape[1]): #column 
#         img[i][j] = [random.randrange(255), random.randrange(255), random.randrange(255)]


# copying and pasting the part of image
tag = img[100:300, 1100:1400] #take image from row 100 to 300 and column 1100 to 1400 and put into variable tag
img[400:600, 600:900] = tag # replace image in tag to image row/height 400 to 600 and column/width 600 to 900

cv2.imshow("manipulate", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
