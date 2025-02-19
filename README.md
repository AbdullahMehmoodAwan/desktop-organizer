# 🖥️ Desktop Organizer Script

## 📌 Overview

This script automatically organizes files on your desktop by sorting them into folders based on their file extensions. It scans the desktop, identifies file types, and moves each file into a corresponding folder.

## ✨ Features

- 📂 Categorizes files based on their extensions.
- 🏷️ Creates necessary folders dynamically (e.g., `jpg_files`, `txt_files`).
- 🚀 Prevents duplication by checking for existing folders.
- 🔍 Skips system files and directories.

## 🛠 Requirements

- 🐍 Python 3.x

## 📥 Installation

1. Ensure Python is installed on your system.
2. Download or copy the `organize_desktop.py` script.

## 🚀 Usage

1. Save the script as `organize_desktop.py`.
2. Open a terminal or command prompt.
3. Navigate to the script's directory:
   ```bash
   cd path/to/script
   python organize_desktop.py
   
## ⚙️ How It Works

- 🖥️ The script retrieves the user's desktop path.
- 📜 It scans for files (ignoring directories).
- 🔖 It extracts file extensions and groups files into corresponding folders.
- 📁 If a folder for a specific extension doesn’t exist, it creates one.
- 🔄 Files are moved into their respective folders.

## 📝 Example

### **Before running the script:**
```plaintext
Desktop/
  document.pdf
  image.jpg
  script.py
  notes.txt

### **After running the script:**
```plaintext
Desktop/
  pdf_files/
    document.pdf
  jpg_files/
    image.jpg
  py_files/
    script.py
  txt_files/
    notes.txt
