import cv2

background = cv2.imread("background.png", cv2.IMREAD_GRAYSCALE)
photo = cv2.imread("photo.png", cv2.IMREAD_GRAYSCALE)
diff = cv2.absdiff(background, photo)
_, diff_wb = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)
cv2.imwrite("test.png", diff_wb)
cv2.imshow("変身", diff_wb)
cv2.waitKey(0)

# diff2 = cv2.medianBlur(diff_wb, 5)
# while True:
#     cv2.imshow("Show", diff2)
