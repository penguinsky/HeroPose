# https://www.blog.umentu.work/python-opencv3%E3%81%A7%E3%83%9E%E3%82%B9%E3%82%AF%E5%90%88%E6%88%90%E7%A9%BA%E9%A3%9B%E3%81%B6%E3%83%80%E3%83%B3%E3%83%9C%E3%83%BC/
import cv2
import math
import numpy as np
import os

# 画像の読み込み
bomb = cv2.imread("bomb2.png", cv2.IMREAD_COLOR)
photo = cv2.imread("photo.png", cv2.IMREAD_COLOR)
bomb = cv2.addWeighted(bomb, 0.9, photo, 1, 0)
orange = cv2.imread("orange.png", cv2.IMREAD_COLOR)
photo = cv2.addWeighted(orange, 0.1, photo, 1, 0)


# マスク画像の読み込み
mask_g = cv2.imread("mask.png", cv2.IMREAD_GRAYSCALE)

# マスク画像を生成する
mask = cv2.merge((mask_g, mask_g, mask_g))

# photo からマスク画像の部分だけを切り出す
photo_m = cv2.bitwise_and(photo, mask)

# マスク画像の白黒を反転
mask_n = cv2.bitwise_not(mask)

# bomb から mask_n の部分を切り出す
bomb_m = cv2.bitwise_and(bomb, mask_n)

# bomb、photo の切り出し画像を合成
img_dst = cv2.bitwise_or(bomb_m, photo_m)

# 表示
cv2.imshow("Show MASK COMPOSITION Image", img_dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
