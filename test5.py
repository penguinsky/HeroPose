# https://qiita.com/Zumwalt/items/fb2e7c20d935803126c7
import cv2

# マスク対象画像読み込み
img = cv2.imread("photo.png", cv2.IMREAD_COLOR)

# マスク画像読み込み
imgMask = cv2.imread("mask.png", cv2.IMREAD_GRAYSCALE)

# マスク画像合成
# マスク画像の明度 0 の画素を灰色（R:128 G:128 B:128）で塗りつぶす
img[imgMask == 0] = [128, 128, 128]

# マスク結果画像を保存
cv2.imwrite("testDstImg.png", img)
