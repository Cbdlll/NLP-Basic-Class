import os
import shutil

def create_category_folders(base_dir, new_dir):
    # 创建类别文件夹
    os.makedirs(os.path.join(new_dir, 'train', 'cat'), exist_ok=True)
    os.makedirs(os.path.join(new_dir, 'train', 'dog'), exist_ok=True)
    os.makedirs(os.path.join(new_dir, 'val', 'cat'), exist_ok=True)
    os.makedirs(os.path.join(new_dir, 'val', 'dog'), exist_ok=True)

def move_images_to_folders(base_dir, new_dir):
    # 移动训练集的图片
    for img_file in os.listdir(os.path.join(base_dir, 'train')):
        img_path = os.path.join(base_dir, 'train', img_file)
        if 'cat' in img_file:
            shutil.move(img_path, os.path.join(new_dir, 'train', 'cat', img_file))
        elif 'dog' in img_file:
            shutil.move(img_path, os.path.join(new_dir, 'train', 'dog', img_file))

    # 移动验证集的图片
    for img_file in os.listdir(os.path.join(base_dir, 'val')):
        img_path = os.path.join(base_dir, 'val', img_file)
        if 'cat' in img_file:
            shutil.move(img_path, os.path.join(new_dir, 'val', 'cat', img_file))
        elif 'dog' in img_file:
            shutil.move(img_path, os.path.join(new_dir, 'val', 'dog', img_file))

if __name__ == "__main__":
    base_directory = 'data'  # 基础目录
    new_directory = 'new_data'  #新目录
    create_category_folders(base_directory, new_directory)
    move_images_to_folders(base_directory, new_directory)
    print("文件重组完成。")
