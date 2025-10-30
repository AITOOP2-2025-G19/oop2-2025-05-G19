import numpy as np
import cv2
from my_module.K21999.lecture05_camera_image_capture import MyVideoCapture

def lecture05_01():

    # カメラキャプチャ実行
    app = MyVideoCapture()
    app.run()
    app.write_img()

    # 画像をローカル変数に保存
    google_img : cv2.Mat = cv2.imread('images/google.png')
    capture_img : cv2.Mat = cv2.imread('output_images/camera_capture.png')

    g_hight, g_width, g_channle = google_img.shape
    c_hight, c_width, c_channel = capture_img.shape
    capture_img = cv2.resize(capture_img, (g_width, g_hight))

    print(google_img.shape)
    print(capture_img.shape)

    for x in range(g_width):
        for y in range(g_hight):
            b, g, r = google_img[y, x]
            # もし白色(255,255,255)だったら置き換える
            if (b, g, r) == (255, 255, 255):
                google_img[y, x] = capture_img[y, x]


    # 書き込み処理
    cv2.imwrite('output_images/lecture05_01_k24128.png', google_img)