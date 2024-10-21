import os
from github import Github

# Retrieve Personal Access Token (PAT) from environment variables
PAT = os.getenv("MY_PAT")
if not PAT:
    raise ValueError("GITHUB_PAT environment variable not set.")

REPO_NAME = "Xtha-Sunil/Numbers"  # Replace with your actual repo name

# Initialize GitHub instance
g = Github(PAT)
repo = g.get_repo(REPO_NAME)

def get_folder_name(num):
    start_range = (num // 100) * 100
    end_range = start_range + 99
    return f"{start_range:04d}-{end_range:04d}/"

def move_files():
    # List all files in the repository
    contents = repo.get_contents("")
    
    while contents:
        file_content = contents.pop(0)
        if file_content.type == "file" and file_content.path.endswith(".txt"):
            file_name = file_content.path.split('/')[-1]
            try:
                # Extract number from the file name (e.g., 0001.txt -> 1)
                number = int(file_name.split('.')[0])

                # Determine the destination folder based on the number
                folder_name = get_folder_name(number)
                new_path = folder_name + file_name

                # Move the file (rename in GitHub's terms)
                repo.rename_file(file_content.path, new_path, f"Moved {file_name} to {folder_name}")
                print(f"Moved {file_name} to {folder_name}")
            
            except Exception as e:
                print(f"Failed to move {file_name}: {e}")

# Run the move operation
move_files()
