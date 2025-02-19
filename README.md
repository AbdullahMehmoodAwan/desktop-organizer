📂 Desktop Organizer
A simple Python script that automatically organizes files on your desktop into categorized folders based on their file extensions. Keep your workspace clean and clutter-free!

🚀 Features
✅ Automatically sorts files into folders (e.g., pdf_files, jpg_files, txt_files)
✅ Skips system folders and files without extensions
✅ Creates folders dynamically based on existing file types
✅ Helps maintain a tidy and organized desktop

🛠️ Requirements
Python 3.x installed on your system
📥 Installation
Clone the repository

sh
Copy
Edit
git clone https://github.com/yourusername/desktop-organizer.git
cd desktop-organizer
Run the script

sh
Copy
Edit
python organize_desktop.py
📌 Example
Before running the script:

lua
Copy
Edit
Desktop/
├── resume.pdf  
├── photo.jpg  
├── notes.txt  
├── script.py  
After running the script:

lua
Copy
Edit
Desktop/
├── pdf_files/  
│     └── resume.pdf  
├── jpg_files/  
│     └── photo.jpg  
├── txt_files/  
│     └── notes.txt  
├── py_files/  
│     └── script.py  
💡 How It Works
The script scans all files on your desktop.
It determines the file type based on its extension.
It creates a folder for each file type (if it doesn’t exist).
It moves the files into their respective folders.
