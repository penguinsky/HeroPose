# https://gist.github.com/astrophysik928/3fde418b2bd30a451703377cb4f49299#file-do_camera-py
import cv2
import datetime

fileName = "photo_" + datetime.datetime.today().strftime('%Y%m%d_%H%M%S') + ".png"

# 内蔵カメラのデバイスIDは0、USBで接続したカメラは1以降。
capture = cv2.VideoCapture(0)

# 取得した画像データは変数imageに格納。retは取得成功変数。
ret, image = capture.read()

if ret:
    # 取得した画像を出力。fileNameは出力する画像名。
    cv2.imwrite(fileName, image)
    print("taking picture is completed!!")
