from PIL import Image
import os

# 画像が保存されているフォルダのパス
image_folder = 'C:\\Users\\jm\\ac\\0009_cloud\\aws\\test_z'
output_pdf = 'output3.pdf'  # 出力するPDFのファイル名

# 画像を開いてリストに追加
image_list = []

# フォルダ内の画像を取得
for filename in os.listdir(image_folder):
    if filename.endswith(".png"):  # 必要に応じて拡張子を追加
        img_path = os.path.join(image_folder, filename)
        img = Image.open(img_path)
        
        # PDF出力のためにRGBモードに変換
        if img.mode == 'RGBA':  # PNGファイルが透明な背景を持つ場合
            img = img.convert('RGB')
        
        image_list.append(img)

# 一つのPDFファイルにまとめて保存
if image_list:
    image_list[0].save(image_folder+"\\"+output_pdf, save_all=True, append_images=image_list[1:])

print(f"{output_pdf} に画像をまとめて保存しました。")
