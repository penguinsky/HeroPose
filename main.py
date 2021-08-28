import cv2
import numpy as np
import time
from playsound import playsound

cam = cv2.VideoCapture(0)


def main():
    cv2.imwrite("backgroundImg.png", getBackground())
    countdown()
    cv2.imwrite("photoImg.png", getPhoto())
    showMixed()

    cam.release()
    cv2.destroyAllWindows()


def getBackground():
    while True:
        if cv2.waitKey(1) == 13:
            break
        cv2.imshow('Photo', get_image(cam))
    return get_image(cam)


def countdown():
    start = time.time()
    while True:
        cv2.waitKey(1)
        diff = 2.9 - time.time() + start
        if diff < 0:
            break
        image = get_image(cam)
        diffStr = ["1", "2", "3"][int(diff)]
        cv2.putText(image, diffStr, (0, 50), cv2.FONT_HERSHEY_PLAIN,
                    4, (255, 0, 0), 5, cv2.LINE_AA)
        cv2.imshow('Photo', image)


def getPhoto():
    img1 = img2 = img3 = get_image(cam)
    th = 300
    lastMoveTime = time.time()
    while True:
        # Enterキーが押されたら終了
        if cv2.waitKey(1) == 13:
            break
        diff = check_image(img1, img2, img3)
        cnt = cv2.countNonZero(diff)
        cv2.imshow('Photo', img3)
        if cnt > th:
            lastMoveTime = time.time()
        if (time.time() - lastMoveTime) > 2:
            # 効果音を鳴らす
            playsound("Onmtp-Flash08-1.mp3", False)
            break
        img1, img2, img3 = (img2, img3, get_image(cam))
    return img3


def showMixed():
    background_gray = cv2.imread("backgroundImg.png", cv2.IMREAD_GRAYSCALE)
    photo_gray = cv2.imread("photoImg.png", cv2.IMREAD_GRAYSCALE)

    # マスク画像を生成する
    #photo_gray = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)
    #background_gray = cv2.cvtColor(background, cv2.COLOR_BGR2GRAY)
    diff = cv2.absdiff(background_gray, photo_gray)
    _, mask = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)
    mask = cv2.merge((mask, mask, mask))

    # 画像の読み込み
    photo = cv2.imread("photoImg.png", cv2.IMREAD_COLOR)
    bomb = cv2.imread("bomb2.png", cv2.IMREAD_COLOR)
    bomb = cv2.addWeighted(bomb, 0.9, photo, 1, 0)
    orange = cv2.imread("orange.png", cv2.IMREAD_COLOR)
    photo = cv2.addWeighted(orange, 0.1, photo, 1, 0)

    # photo からマスク画像の部分だけを切り出す
    photo_m = cv2.bitwise_and(photo, mask)

    # マスク画像の白黒を反転
    mask_n = cv2.bitwise_not(mask)

    # bomb から mask_n の部分を切り出す
    bomb_m = cv2.bitwise_and(bomb, mask_n)

    # bomb、photo の切り出し画像を合成
    img_dst = cv2.bitwise_or(bomb_m, photo_m)

    # 表示
    cv2.imshow("Photo", img_dst)
    cv2.waitKey(0)


def check_image(img1, img2, img3):  # 画像に動きがあったか調べる関数
    # グレイスケール画像に変換 --- (*6)
    gray1 = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)
    gray3 = cv2.cvtColor(img3, cv2.COLOR_RGB2GRAY)
    # 絶対差分を調べる --- (*7)
    diff1 = cv2.absdiff(gray1, gray2)
    diff2 = cv2.absdiff(gray2, gray3)
    # 論理積を調べる --- (*8)
    diff_and = cv2.bitwise_and(diff1, diff2)
    # 白黒二値化 --- (*9)
    _, diff_wb = cv2.threshold(diff_and, 30, 255, cv2.THRESH_BINARY)
    # ノイズの除去 --- (*10)
    diff = cv2.medianBlur(diff_wb, 5)
    return diff


def get_image(cam):  # カメラから画像を取得する
    img = cam.read()[1]
    img = cv2.resize(img, (640, 480))
    return img


main()
