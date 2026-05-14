import os

folder = r"D:\Office\Automation_learning\test_folder"

print("Checking folder:", folder)
files = os.listdir(folder)
print("Files found:", files)
pdf = r"D:\Office\Automation_learning\test_folder\PDF"
image = r"D:\Office\Automation_learning\test_folder\Images"
text = r"D:\Office\Automation_learning\test_folder\Text"
audio = r"D:\Office\Automation_learning\test_folder\Audio"

for path in [pdf, image, text, audio]:
    os.makedirs(path, exist_ok=True)

for file in files:
    old_path = os.path.join(folder, file)
    if os.path.isdir(old_path):
        continue
    root, ext = os.path.splitext(file)
    if ext == ".pdf":
        new_path = os.path.join(pdf, f"{file}")
        os.rename(old_path, new_path)
    elif ext == ".jpg":
        new_path = os.path.join(image, f"{file}")
        os.rename(old_path, new_path)
    elif ext == ".txt":
        new_path = os.path.join(text, f"{file}")
        os.rename(old_path, new_path)
    else:
        new_path = os.path.join(audio, f"{file}")
        os.rename(old_path, new_path)

print("Done.")