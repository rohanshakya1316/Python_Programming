# Strings introduction in Python
# Strings are immuatable i.e., cannot be change

name = 'Rohan Shakya'   # Single quoted string
full_name = "Rohan Man Shakya"   # Double quoted string
temp = '''Rohan Man Shakya'''   # Triple single quoted string
me = """Rohan Man Shakya"""   # Triple double quoted string


print(name)
print(full_name)
print(len(temp))    # find the length of the string
print(me)

# String Slicing  
# Syntax: string[start:end:step]
# start: index to begin the slice (inclusive)

# end: index to end the slice (exclusive)

# step: optional, default is 1 (can skip characters)


short_name = name[0]   # first character 
print(short_name)
end_name = name[-1]   # last character
print(end_name)

name_part = full_name[0 : 9]  # start from index 0 till 8 (excludes 9) 
print(name_part)

end_part = full_name[-9 : -1]  # start from index -9 till -2 backward (excludes -1) 
print(end_part)

# slicing program 

text = input("Enter a string: ")

print("\n--- String Slicing Examples ---")
print("Original string:", text)

print("text[0:5]    =", text[0:5])     # First 5 characters
print("text[2:]     =", text[2:])      # From index 2 to end
print("text[:5]     =", text[:5])      # From start to index 4
print("text[-3:]    =", text[-3:])     # Last 3 characters
print("text[:-3]    =", text[:-3])     # All except last 3
print("text[::2]    =", text[::2])     # Every 2nd character
print("text[::-1]   =", text[::-1])    # Reverse the string
