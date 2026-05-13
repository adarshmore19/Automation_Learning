import os

folder = r"D:\Office\Automation_learning\test_folder"

print("Checking folder:", folder)

files = os.listdir(folder)
print("Files found:", files)
prefix = input("Enter file prefix: ")

for i, file in enumerate(files):
    old_path = os.path.join(folder, file)
    new_path = os.path.join(folder, f"{prefix}_{i}.txt")

    os.rename(old_path, new_path)
    print(f"Renamed {file} -> {prefix}_{i}.txt")

print("Done.")