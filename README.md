Desktop Organizer Script

Overview

This script automatically organizes files on your desktop by sorting them into folders based on their file extensions. It scans the desktop, identifies file types, and moves each file into a corresponding folder.

Features

Categorizes files based on their extensions.

Creates necessary folders dynamically (e.g., jpg_files, txt_files).

Prevents duplication by checking for existing folders.

Skips system files and folders.

Requirements

Python 3.x

Installation

Ensure Python is installed on your system.

Download or copy the organize_desktop.py script.

Usage

Save the script as organize_desktop.py.

Open a terminal or command prompt.

Navigate to the script's directory:

cd path/to/script

Run the script:

python organize_desktop.py

How It Works

The script retrieves the user's desktop path.

It scans for files (ignoring directories).

It extracts file extensions and groups files into corresponding folders.

If a folder for a specific extension doesn’t exist, it creates one.

Files are moved into their respective folders.

Example

Before running the script:

Desktop/
  document.pdf
  image.jpg
  script.py
  notes.txt

After running the script:

Desktop/
  pdf_files/
    document.pdf
  jpg_files/
    image.jpg
  py_files/
    script.py
  txt_files/
    notes.txt

Notes

Ensure that you have the necessary permissions to modify files on your desktop.

The script does not overwrite or rename existing files.

If a file has no extension, it will not be moved.

License

This script is open-source and free to use. Modify as needed!

