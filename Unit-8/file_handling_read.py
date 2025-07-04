# File Handling in Python

# Opening file in python. 

# open("filename", 'mode') == To open a file for reading.
#  
# There are four different methods (modes) for opening a file:

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist

# "a" - Append - Opens a file for appending, creates the file if it does not exist

# "w" - Write - Opens a file for writing, creates the file if it does not exist

# "x" - Create - Creates the specified file, returns an error if the file exists

# In addition you can specify if the file should be handled as binary or text mode

# "t" - Text - Default value. Text mode

# "b" - Binary - Binary mode (e.g. images)

file = open("Unit-8/file_read.txt")     # open() = opens a file and return a file object.

# file = open("Unit-8/file_read.txt", "rt")   ------> Same as line 23 as 'rt' is default value of open()

print(file.read())      # read() = method for reading the content of file

file.close()


# with statement

# The best way to open and close the file automatically is the with statement.

with open("Unit-8/file_read.txt") as f:
    text = f.read()
    print(text, type(text))

# f.close() not needed as it is automatically closed.


# Read Only Parts of the File 
# By default the read() method returns the whole text, but we can also specify how many characters we want to return:

with open("Unit-8/file_read.txt") as fptr:
    print(fptr.read(13))    # Return the 13 first characters of the file:

