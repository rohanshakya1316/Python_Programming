# Write a program to detect double space in a string and replace it with single space.  

str = "Hi! My name is Rohan Shakya. "

dblstr = "Hello!  I am learning  Python"

print("If negative index is returned then there is no occurrence")
print(str.find("  ")) 


print("If positive index is returned then there is the occurrence")
print(dblstr.find("  "))

print(dblstr)
print(dblstr.replace("  ", " ")) # it returns new string as strings are immuatable 

print(dblstr)