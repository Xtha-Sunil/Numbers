import os
import subprocess

# Get all .txt files in the current directory
files = [f for f in os.listdir() if f.endswith('.txt')]

def get_folder_name(num):
    start_range = (num // 100) * 100
    end_range = start_range + 99
    return f"{start_range:04d}-{end_range:04d}"

# Loop through files and move them to corresponding folders
for file in files:
    try:
        # Extract the number from the file name (e.g., 0001.txt -> 1)
        number = int(file.split('.')[0])

        # Determine folder name
        folder = get_folder_name(number)

        # Create the folder if it doesn't exist
        if not os.path.exists(folder):
            os.makedirs(folder)

        # Move the file using git mv
        subprocess.run(['git', 'mv', file, f'{folder}/{file}'])

        print(f"Moved {file} to {folder}/{file}")

    except Exception as e:
        print(f"Failed to move {file}: {e}")

# Commit the changes
subprocess.run(['git', 'commit', '-m', 'Moved number files into folders based on range'])
