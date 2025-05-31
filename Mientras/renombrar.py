import os

image_exts = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp'}
files = [f for f in os.listdir('.') if os.path.isfile(f) and os.path.splitext(f)[1].lower() in image_exts]
files.sort()
for idx, filename in enumerate(files, 1):
    ext = os.path.splitext(filename)[1]
    new_name = f"img{idx}{ext}"
    os.rename(filename, new_name)