# https://www.blog.umentu.work/python-opencv3%E3%81%A7%E3%83%9E%E3%82%B9%E3%82%AF%E5%90%88%E6%88%90%E7%A9%BA%E9%A3%9B%E3%81%B6%E3%83%80%E3%83%B3%E3%83%9C%E3%83%BC/
import cv2
import math
import numpy as np
import os

# 画像の読み込み
img_src1 = cv2.imread("./image/sora.jpg", 1)
img_src2 = cv2.imread("./image/dambo3.jpg", 1)

# ダンボー画像をグレースケール化
img2_gray = cv2.cvtColor(img_src2, cv2.COLOR_BGR2GRAY)


# マスク画像を生成するために二値化
img_maskg = cv2.threshold(img2_gray, 220, 255, cv2.THRESH_BINARY_INV)[1]

# マスク画像を生成する
img_mask = cv2.merge((img_maskg, img_maskg, img_maskg))

# img_src2からマスク画像の部分だけを切り出す
img_src2m = cv2.bitwise_and(img_src2, img_mask)


# マスク画像の白黒を反転
img_maskn = cv2.bitwise_not(img_mask)

# img_src1からimg_msknの部分を切り出す
img_src1m = cv2.bitwise_and(img_src1, img_maskn)

# img_src1、img_src2の切り出し画像を合成
img_dst = cv2.bitwise_or(img_src1m, img_src2m)


# 表示
cv2.imshow("Show MASK COMPOSITION Image", img_dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
