import cv2  # pip install opencv-python

save_path = "./img"
def main():
    cam = cv2.VideoCapture(0)
    img1 = img2 = img3 = get_image(cam)
    th = 300
    num = 1
    while True:
        if cv2.waitKey(1) == 13:    # Enterキーが押されたら終了
            break
        diff = check_image(img1, img2, img3)    # 差分を調べる
        cnt = cv2.countNonZero(diff)
        if cnt > th:
            print("カメラに動きを検出")
            cv2.imshow('PUSH ENTER KEY', img3)
            cv2.imwrite(save_path + str(num) + ".jpg", img3)
            num += 1
        else:
            cv2.imshow('PUSH ENTER KEY', diff)
        img1, img2, img3 = (img2, img3, get_image(cam))
    cam.release()
    cv2.destroyAllWindows() 

# 画像に動きがあったか調べる関数
def check_image(img1, img2, img3):
    gray1 = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)  # グレイスケール画像に変換
    gray2 = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)
    gray3 = cv2.cvtColor(img3, cv2.COLOR_RGB2GRAY)

    diff1 = cv2.absdiff(gray1, gray2)   # 絶対差分を調べる
    diff2 = cv2.absdiff(gray2, gray3)

    diff_and = cv2.bitwise_and(diff1, diff2)    # 論理積を調べる
    _, diff_wb = cv2.threshold(diff_and, 30, 255, cv2.THRESH_BINARY)
    diff = cv2.medianBlur(diff_wb, 5)
    return diff

# カメラから画像を取得する
def get_image(cam):
    img = cam.read()[1]
    img = cv2.resize(img, (600, 400))
    return img

if __name__ == '__main__':
    main()