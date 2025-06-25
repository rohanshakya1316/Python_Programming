# Write a python program to print the contents of a directory using the os module. 
# search online for the function which does that. 
import os

# Specify the path of the directory
directory_path = "D:" 

try:
    # Get the list of files and directories
    contents = os.listdir(directory_path)

    # Print each file and directory name
    print(f"Contents of '{directory_path}':")
    for item in contents:
        print(item)

except FileNotFoundError:
    print("The specified directory does not exist.")
except PermissionError:
    print("Permission denied to access the directory.")
