# Delete a File

# To delete a file, import the OS module, and run its os.remove() function. 

import os

os.remove("Unit-8/demofile.txt") 



# Check existence of the file
# To overwrite the existing content to the file, use the w parameter:

if os.path.exists("Unit-8/demofile.txt"):
    os.remove("Unit-8/demofile.txt")
    print("Successfully deleted!")
else:
    print("The file does not exists.")


# Delete Folder (Must be an empty folder to be deleted)

os.rmdir("Unit-8/myfolder")