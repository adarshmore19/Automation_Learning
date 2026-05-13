import os  # Import the 'os' module for operating system interactions like file operations

# Define the folder path as a raw string to handle Windows path backslashes correctly
folder = r"D:\Office\Automation_learning\test_folder"

# Print message to indicate we're checking the specified folder
print("Checking folder:", folder)

# Get a list of all files in the specified folder
files = os.listdir(folder)
# Print the files found in the folder
print("Files found:", files)
# Prompt user to enter a custom prefix for the renamed files
prefix = input("Enter file prefix: ")

# Loop through each file in the list with its index
for i, file in enumerate(files):
    # Create the full path of the original file by joining folder path and filename
    old_path = os.path.join(folder, file)
    # Create the new path with custom prefix provided by the user (prefix_0.txt, prefix_1.txt, etc.)
    new_path = os.path.join(folder, f"{prefix}_{i}.txt")

    # Rename the file from old_path to new_path
    os.rename(old_path, new_path)
    # Print confirmation message showing the old and new filename
    print(f"Renamed {file} -> {prefix}_{i}.txt")

# Print completion message
print("Done.")
