import os
import shutil
from datetime import datetime

def generate_timestamp():
    return datetime.now().strftime('%d%m%y_%H%M%S')

def backup_files(src_dir, dest_dir):
    if not os.path.isdir(src_dir):
        print(f"Error: Source directory '{src_dir}' does not exist.")
        return
    if not os.path.isdir(dest_dir):
        print(f"Error: Destination directory '{dest_dir}' does not exist.")
        return

    for root, dirs, files in os.walk(src_dir):
        rel_path = os.path.relpath(root, src_dir)
        dest_subdir = os.path.join(dest_dir, rel_path) if rel_path != '.' else dest_dir
        os.makedirs(dest_subdir, exist_ok=True)

        for filename in files:
            src_file = os.path.join(root, filename)
            dest_file = os.path.join(dest_subdir, filename)

            if os.path.exists(dest_file):
                name, ext = os.path.splitext(filename)
                timestamp = generate_timestamp()
                new_filename = f"{name}_{timestamp}{ext}"
                dest_file = os.path.join(dest_subdir, new_filename)

            try:
                shutil.copy2(src_file, dest_file)
                print(f"Copied '{src_file}' to '{dest_file}'")
            except Exception as e:
                print(f"Error copying '{src_file}': {e}")

if __name__ == "__main__":
    src_dir = r"C:\Users\Prakash\Desktop\File Copy"
    dest_dir = r"C:\Users\Prakash\Documents\Test Backup"
    backup_files(src_dir, dest_dir)
