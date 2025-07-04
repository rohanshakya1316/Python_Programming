#  Write a python program to rename a file to “renamed_by_ python.txt.

import os

# Specify the current file name and the new name
old_name = 'PracticeQuestions/Problem9/newfile.txt'         # Replace with the actual current file name
new_name = "PracticeQuestions/Problem9/renamed_by_python.txt"

try:
    os.rename(old_name, new_name)
    print(f"File renamed from '{old_name}' to '{new_name}' successfully.")
except FileNotFoundError:
    print(f"Error: The file '{old_name}' does not exist.")
except PermissionError:
    print("Error: You do not have permission to rename this file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# If you want to rename a file using shutil (from Python's standard library), it's actually better to use the built-in os.rename() or shutil.move(), because shutil is mainly for copying and moving files, not specifically for renaming.


import shutil

# Old file name
old_name = "your_file.txt"  # Replace with your file
# New file name
new_name = "renamed_by_python.txt"

try:
    shutil.move(old_name, new_name)
    print(f"File renamed successfully to '{new_name}'")
except FileNotFoundError:
    print(f"Error: File '{old_name}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")

