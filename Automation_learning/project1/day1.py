import os  # Import the 'os' module for operating system interactions like file operations

# Define the folder path as a raw string to handle Windows path backslashes correctly
folder = r"D:\Office\Automation_learning\test_folder"

# Print message to indicate we're checking the specified folder
print("Checking folder:", folder)

# Get a list of all files in the specified folder
files = os.listdir(folder)
# Print the files found in the folder
print("Files found:", files)

# Loop through each file in the list with its index (i: 0, 1, 2, ...)
for i, file in enumerate(files):
    # Create the full path of the original file by joining folder path and filename
    old_path = os.path.join(folder, file)
    # Create the new path with a generic naming pattern (file_0.txt, file_1.txt, etc.)
    new_path = os.path.join(folder, f"file_{i}.txt")

    # Rename the file from old_path to new_path using os.rename()
    os.rename(old_path, new_path)
    # Print confirmation message showing the old and new filename
    print(f"Renamed {file} -> file_{i}.txt")

# Print completion message
print("Done.")
