from PIL import Image, ImageFilter
import os

# フォルダのパスを設定
input_folder = 'C:\\Users\\jm\\ac\\0009_cloud\\aws\\test_y'
output_folder = 'C:\\Users\\jm\\ac\\0009_cloud\\aws\\test_z'

# トリミングする上部のピクセル数
crop_height = 160  # 例として上から50ピクセルをトリミング

# 出力フォルダが存在しない場合、作成
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# フォルダ内の画像を処理
for filename in os.listdir(input_folder):
    if filename.endswith(".png"):  # 必要に応じて拡張子を追加
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)
        
        # 画像サイズ取得
        width, height = img.size
        
        # 上部をトリミング（crop関数の引数は左, 上, 右, 下の順）
        #cropped_img = img.crop((0, 160, width, height-70)).filter(ImageFilter.SHARPEN)
        #cropped_img = img.crop((0, 160, width, height-70))
        
        # トリミングした画像を保存
        output_path = os.path.join(output_folder, filename)
        img.filter(ImageFilter.SHARPEN).save(output_path)
        print(f"{filename} をトリミングして保存しました。")

print("すべての画像のトリミングが完了しました。")
