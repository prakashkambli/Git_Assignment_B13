This repository contains Python scripts for common utility tasks such as file backup, CPU checks, and password strength validation.

📁 Repository Contents
Backup.py
Recursively copies all files (including subdirectories) from a specified source folder to a destination folder. If a file with the same name exists in the destination, it appends a timestamp (ddmmyy_hhmmss) to the filename for uniqueness.

CPU Check.py
Checks the CPU usage of the system (add more details based on your script).

CPU Check 1.py
Alternate or additional CPU check script (add more details if needed).

check_password_strength.py
Script to assess and validate the strength of user passwords.

🛠️ How to Use
Backup.py
Function:
Recursively backs up all files and folders from the source to the destination, ensuring no files are overwritten by appending a timestamp if needed.

Default Folders:

Source:
C:\Users\Prakash\Desktop\File Copy

Destination:
C:\Users\Prakash\Documents\Test Backup

To run:

bash
python Backup.py
You can modify the source and destination paths inside Backup.py if needed.

CPU Check & Password Strength Scripts
To run any script:

bash
python script_name.py
For usage instructions, see the respective script file comments.

📝 How to Run All Scripts
Note: Make sure you have Python 3.x installed.

Clone the repository:

bash
git clone https://github.com/prakashkambli/Git_Assignment_B13.git
cd your-repo
Run the desired script as shown above.

💡 Notes
The Backup.py script preserves subdirectory structure and uses timestamps in ddmmyy_hhmmss format.

Error handling is included for missing directories and file I/O issues.

Scripts are written for Windows file paths, but logic can be adjusted for other platforms.

📄 License
This project is for educational/demo purposes.
Feel free to modify and use in your own projects.

👤 Author
Prakash Kambli.

Feel free to open issues or submit pull requests for improvements or bug fixes!
