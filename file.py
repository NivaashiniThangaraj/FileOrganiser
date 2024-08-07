import os
import shutil

# Define file types and target directories
FILE_TYPES = {
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv'],
    'Music': ['.mp3', '.wav', '.aac'],
}

TARGET_DIRECTORIES = {
    'Documents': 'Documents',
    'Images': 'Images',
    'Videos': 'Videos',
    'Music': 'Music',
    'Others': 'Others'
}

def move_files(src_folder, dest_folder):
    if not os.path.exists(src_folder):
        print(f"Source folder does not exist: {src_folder}")
        return

    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
        print(f"Created destination folder: {dest_folder}")

    for filename in os.listdir(src_folder):
        src = os.path.join(src_folder, filename)
        if os.path.isfile(src):
            file_extension = os.path.splitext(filename)[1].lower()
            target_dir = 'Others'
            for category, extensions in FILE_TYPES.items():
                if file_extension in extensions:
                    target_dir = TARGET_DIRECTORIES[category]
                    break

            target_path = os.path.join(dest_folder, target_dir)
            if not os.path.exists(target_path):
                os.makedirs(target_path)

            destination = os.path.join(target_path, filename)
            if os.path.exists(destination):
                destination = handle_duplicates(destination)

            print(f"Moving {src} to {destination}")
            shutil.move(src, destination)

def handle_duplicates(path):
    filename, extension = os.path.splitext(path)
    counter = 1
    new_path = f"{filename}_{counter}{extension}"
    while os.path.exists(new_path):
        counter += 1
        new_path = f"{filename}_{counter}{extension}"
    return new_path

# Define folder paths
folder_to_track = r"C:\Users\NIVAASHINI\Desktop\SOURCE"
folder_destination = r"C:\Users\NIVAASHINI\Desktop\ORGANISED-2"

# Move files from source to destination
move_files(folder_to_track, folder_destination)

