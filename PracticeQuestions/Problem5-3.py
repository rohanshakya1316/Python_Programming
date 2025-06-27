# What will be the length of following set s: 
# s = set() 
# s.add(20) 
# s.add(20.0) 
# s.add('20') # length of s after these operations?

s = set() 
s.add(20) 
s.add(20.0)         # 20 == 20.0  True in python
s.add('20')

print("Length of s:", len(s))   # output: 2
print("Set is", s)              # { 20, '20'}

# What is the type of 's'?
s = {}
print(type(s))  # output: <class 'dict' >