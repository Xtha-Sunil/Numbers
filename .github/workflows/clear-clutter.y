name: Move Files in Repo

on:
  workflow_dispatch:
    inputs:
      branch:
        description: 'feat:clear-clutter'
        required: true
        default: 'main'

jobs:
  move_files:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout Repository
      uses: actions/checkout@v3

    - name: Run Python Script
      env:
        MY_PAT: ${{ secrets.MY_PAT }}
      run: |
        pip install PyGithub
        python -c "
from github import Github

PAT = '${{ secrets.MY_PAT }}'
REPO_NAME = 'Xtha-Sunil/Numbers'
g = Github(PAT)
repo = g.get_repo(REPO_NAME)

def get_folder_name(num):
    start_range = (num // 100) * 100
    end_range = start_range + 99
    return f'{start_range:04d}-{end_range:04d}/'

def move_files():
    contents = repo.get_contents('')
    while contents:
        file_content = contents.pop(0)
        if file_content.type == 'file' and file_content.path.endswith('.txt'):
            file_name = file_content.path.split('/')[-1]
            try:
                number = int(file_name.split('.')[0])
                folder_name = get_folder_name(number)
                new_path = folder_name + file_name
                repo.rename_file(file_content.path, new_path, f'Moved {file_name} to {folder_name}')
                print(f'Moved {file_name} to {folder_name}')
            except Exception as e:
                print(f'Failed to move {file_name}: {e}')
move_files()
        "
