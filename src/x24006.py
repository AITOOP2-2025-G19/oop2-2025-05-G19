import numpy as np
import cv2
from my_module.K21999.lecture05_camera_image_capture import MyVideoCapture

def lecture05_01():

    # カメラキャプチャ実行
    app = MyVideoCapture()
    app.run()

    # 画像をローカル変数に保存
    google_img : cv2.Mat = cv2.imread('images/google.png')
    capture_img : cv2.Mat = app.get_img()


    # 🚨 画像読み込みチェック 🚨
    if google_img is None:
        print("エラー: 'images/google.png' の読み込みに失敗しました。ファイルパスを確認してください。")
        return
    if capture_img is None:
        print("エラー: 'images/camera_capture.png' の読み込みに失敗しました。ファイルパスを確認してください。")
        return # このチェックは 'capture_img : cv2.Mat = "implement me"' への対応として残すか検討
    
    #画像のメタ情報
    g_hight, g_width, g_channel = google_img.shape
    c_hight, c_width, c_channel = capture_img.shape
    print(google_img.shape)
    print(capture_img.shape)
    new_img = np.zeros((g_hight, g_width, g_channel), dtype=np.uint8)

    #画素操作
    for x in range(g_width):
        for y in range(g_hight):
            b, g, r = google_img[y, x]
            # もし白色(255,255,255)だったら置き換える
            if (b, g, r) == (255, 255, 255):
                pass
                y_cap = y % c_hight
                # x (0-1279) を c_width (640) で割った余りを取得 -> 0-639 の範囲に収まる
                x_cap = x % c_width
                b, g, r = capture_img[y_cap, x_cap]

    #操作した画素を代入    
    new_img[y, x] = [b, g, r]

    # 書き込み処理
    if new_img is None:
        raise ValueError("キャプチャ画像が存在しません。run()を実行してから保存してください。")

    cv2.imwrite('output_images/lecture05_01_X24006.png', new_img)
