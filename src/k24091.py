import numpy as np
import cv2
import os
from my_module.K21999.lecture05_camera_image_capture import MyVideoCapture

def lecture05_01():

    # カメラキャプチャ実行
    app = MyVideoCapture()
    app.run()

    # 画像をローカル変数に保存
    google_img : cv2.Mat = cv2.imread('images/google.png')
    capture_img : cv2.Mat = cv2.imread('images/camera_capture.png') # 動作テスト用なので提出時にこの行を消すこと
    # capture_img : cv2.Mat = "implement me"

    g_hight, g_width, g_channel = google_img.shape
    c_hight, c_width, c_channel = capture_img.shape
    print(google_img.shape)
    print(capture_img.shape)

    capture_img_resized = cv2.resize(
        (g_width, g_hight), 
        interpolation=cv2.INTER_LINEAR
    )
    new_img = np.zeros((g_hight, g_width, g_channel), dtype=np.uint8)

    for x in range(g_width):
        for y in range(g_hight):
            b, g, r = google_img[y, x]
            # もし白色(255,255,255)だったら置き換える
            if (b, g, r) == (255, 255, 255):
                pass
                b_c, g_c, r_c = capture_img_resized[y,x]

                new_img[y,x] = [b_c, g_c, r_c]
            else:
                new_img[y, x] = [b, g, r]

                
    new_img[y,x] = [b, g, r]
    
    # 書き込み処理
    # 出力ディレクトリとファイル名の設定
    output_dir = os.path.join(project_root, 'output_images')
    os.makedirs(output_dir, exist_ok=True)
    
    output_path = os.path.join(output_dir, 'lecture05_01_k24091.png')
    
    # cv2.imwrite の第2引数にはファイル名（パスを含む）を指定する必要がある
    cv2.imwrite(output_path, new_img)
    print(f"処理が完了しました。画像は '{output_path}' に保存されました。")

