# Import the os module for file and directory operations
import os

# Define the root folder path where files will be organized
folder = r"D:\Office\Automation_learning\test_folder"

# Display the folder being checked
print("Checking folder:", folder)
# List all files and subdirectories in the specified folder
files = os.listdir(folder)
# Display the files found in the folder
print("Files found:", files)

# Define paths for different file type subdirectories
pdf = r"D:\Office\Automation_learning\test_folder\PDF"
image = r"D:\Office\Automation_learning\test_folder\Images"
text = r"D:\Office\Automation_learning\test_folder\Text"
audio = r"D:\Office\Automation_learning\test_folder\Audio"

# Create all required subdirectories if they don't already exist
# exist_ok=True prevents errors if directories already exist
for path in [pdf, image, text, audio]:
    os.makedirs(path, exist_ok=True)

# Iterate through each file in the folder to organize by file type
for file in files:
    # Create the full path to the current file
    old_path = os.path.join(folder, file)
    # Skip if the current item is a directory
    if os.path.isdir(old_path):
        continue
    # Extract the file name and file extension
    root, ext = os.path.splitext(file)
    # Check file extension and move to appropriate folder
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
        # Move any other file types to the audio folder by default
        new_path = os.path.join(audio, f"{file}")
        os.rename(old_path, new_path)

# Display completion message
print("Done.")
