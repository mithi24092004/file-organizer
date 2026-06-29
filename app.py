import os
import shutil


FOLDER_PATH = os.path.join(os.path.expanduser("~"), "Desktop")

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Audio": [".mp3", ".wav"],
}

def create_folders():
    """Create required folders if not exist"""
    for folder in FILE_TYPES.keys():
        os.makedirs(os.path.join(FOLDER_PATH, folder), exist_ok=True)

    os.makedirs(os.path.join(FOLDER_PATH, "Others"), exist_ok=True)


def organize_files():
    """Organize files into folders"""
    files = os.listdir(FOLDER_PATH)

    for file in files:
        file_path = os.path.join(FOLDER_PATH, file)

        # Skip folders
        if os.path.isdir(file_path):
            continue

        moved = False

        for folder_name, extensions in FILE_TYPES.items():
            if file.lower().endswith(tuple(extensions)):
                shutil.move(file_path, os.path.join(FOLDER_PATH, folder_name, file))
                print(f"Moved: {file} -> {folder_name}")
                moved = True
                break

        if not moved:
            shutil.move(file_path, os.path.join(FOLDER_PATH, "Others", file))
            print(f"Moved: {file} -> Others")


if __name__ == "__main__":
    print("Organizing folder:", FOLDER_PATH)
    create_folders()
    organize_files()
    print("Done! Files organized successfully.")