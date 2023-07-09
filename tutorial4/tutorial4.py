# drawing line, rectangle, circle, image and text
# koordinat pada open cv x = dari kiri ke kanan dan y = dari atas ke bawah

import cv2

cap = cv2.VideoCapture(0)
width = int(cap.get(3))
height = int(cap.get(4))


while True:
    ret, frame = cap.read()

    # drawing line
    # cv2.line(src/frame, start_coordinat, end_coordinate, color, thickness/ketebalan)
    img = cv2.line(frame, (0, 0), (width, height), [255, 0, 0], 10) #gambar garis warna biru dari atas kiri ke bawah kanan
    img = cv2.line(img, (0, height), (width, 0), [0, 0, 255], 5) #menambah garis warna merah dari bawah kanan ke atas kiri

    # drawing rectangle
    # cv2.rectangle(src/frame, start_coordinat, end_coordinate, color, thickness/ketebalan) ps: ketebalan fill = -1
    img = cv2.rectangle(img, (100, 100), (200,200), [127, 0, 255], 5) # ketebalan jika menggunakan -1 akan fill semua warna ke gambar jika tidak cuman garisnya saja

    #drawing circle
    # cv2.circle(src/frame, center_coordinate, radius, color, thickness/ketebalan)
    img = cv2.circle(img, (320, 240), 60, [0, 255, 0], -1) # ketebalan menggunakan -1 maka warna akan fill semua pada lingkaran

    # put some text
    # make font first
    font = cv2.FONT_ITALIC
    # make text
    # cv2.putText(src/frame, text, center_position(bottom left text), font, font scale, color, thickness/ketebalan, Line_Type)
    img = cv2.putText(img, "Hayuu Orbit", (50, height - 20), font, 2, [237, 149, 100], 3, cv2.LINE_AA)

    # ellipse
    img = cv2.ellipse(img, (256,256), (100, 50), 0, 0, 180, [255, 0, 0], -1)

    cv2.imshow("Camera", img)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.release()
cv2.destroyAllWindows()


