import os
import shutil

def organize_desktop():
    """
    Organizes files on the desktop by grouping them into folders based on file extensions.
    """

    # Get the path to the user's desktop directory
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

    # Ensure the desktop path exists (should always be true on a normal system)
    if not os.path.exists(desktop_path):
        print("Error: Desktop path not found!")
        return

    # List all items on the desktop (files and folders)
    items = os.listdir(desktop_path)

    # Loop through each item on the desktop
    for item in items:
        item_path = os.path.join(desktop_path, item)

        # Skip directories since we only want to move files
        if os.path.isdir(item_path):
            continue

        # Extract the file extension (e.g., ".txt", ".jpg") and remove the dot
        file_extension = os.path.splitext(item)[1][1:]

        # Skip files that have no extension (e.g., system files, executables without extensions)
        if not file_extension:
            continue

        # Normalize extension to lowercase for consistency (e.g., "JPG" → "jpg")
        file_extension = file_extension.lower()

        # Define a folder name based on the file extension
        destination_folder = os.path.join(desktop_path, file_extension + "_files")

        # Create the folder if it doesn't already exist
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        # Move the file to the corresponding folder
        shutil.move(item_path, os.path.join(destination_folder, item))

    print("Desktop organization complete!")

if __name__ == "__main__":
    # Call the function to organize desktop files
    organize_desktop()

"""
# Instructions to Run This Script:

1. Ensure you have Python installed (Python 3.x recommended).
2. Save this script as 'organize_desktop.py'.
3. Open a terminal or command prompt.
4. Navigate to the script's directory using `cd` command.
5. Run the script with:
   ```sh
   python organize_desktop.py
"""
