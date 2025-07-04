# Read Lines 

# We can return one line by using the readline() method.

with open("Unit-8/file_read.txt") as f: 
    line1 = f.readline()    # returns one line 
    line2 = f.readline()
    line3 = f.readline()
    print(line1, type(line2))   # type: < str > 
    print(line2, type(line2))   # type: < str > 
    print(line3, type(line3))   # type: < str > 

# By looping through the lines of the file, we can read the whole file line by line: 
with open("Unit-8/file_read.txt") as fptr: 
    # Using for loop
    for x in fptr: 
        print(x, type(x))

    # Using while loop
    line = fptr.readline()
    while line != "":
        print(line, type(line))
        line = fptr.readline()


with open("Unit-8/file_read.txt") as fptr: 
    line_list = fptr.readlines()    # returns list of lines
    print(line_list, type(line_list))   # type: < list > 