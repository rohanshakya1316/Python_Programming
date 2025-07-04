# Write in file 

# 1. Create a New File 

# To create a new file in Python, use the open() method, with one of the following parameters:

# "x" - Create - will create a file, returns an error if the file exists

# "a" - Append - will create a file if the specified file does not exists

# "w" - Write - will create a file if the specified file does not exists


# Create a new file named myfile.txt
# If the file already exits, an error occurs.
 
# f = open('Unit-8/myfile.txt', 'x') 


# 2. Write to an Existing File 

# To write to an existing file, you must add a parameter to the open() function:
# "a" - Append - will append to the end of the file
with open("Unit-8/myfile.txt", 'a') as f:
    f.write("\nI am new line being appended here.")

# open and read the file after the appending
with open("Unit-8/myfile.txt") as f: 
    text = f.read()
    print(text)


# 3. Overwrite Existing Content

# To overwrite the existing content to the file, use the w parameter:
# "w" - Write - will overwrite any existing content
with open("Unit-8/myfile.txt", "w") as f:
    f.write("I am overwritten here.")

# open and read the file after the overwriting: 
with open("Unit-8/myfile.txt") as f:
    line = f.read()
    print(line)

