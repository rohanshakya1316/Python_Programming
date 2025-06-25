# strings functions

s = "  Hello, World!  "

# Case changing
print(s.lower()     )    # '  hello, world!  '
print(s.upper()     )    # '  HELLO, WORLD!  '
print(s.capitalize())    # '  hello, world!  '
print(s.title()     )    # '  Hello, World!  '
print(s.swapcase()  )    # '  hELLO, wORLD!  '

# Whitespace handling
print(s.strip() )        # 'Hello, World!'
print(s.lstrip())        # 'Hello, World!  '
print(s.rstrip())        # '  Hello, World!'

# Searching
print(s.find("World") )  # 9
print(s.index("World"))  # 9 (raises error if not found)
print(s.rfind("l")    )  # Last index of 'l'
print(s.count("l")    )  # 3

# Replacing
print(s.replace("Hello", "Hi"))  # '  Hi, World!  '

# Checking conditions
print(s.startswith("  He"))   # True
print(s.endswith("!  ")   )   # True
print("123".isdigit()     )   # True
print("abc".isalpha()     )   # True
print("abc123".isalnum()  )   # True
print("   ".isspace()     )   # True

# Formatting and joining
print(".".join(["a", "b", "c"]) )     # 'a.b.c'
print("hello {}".format("world"))    # 'hello world'

# Splitting
print("apple,banana,orange".split(","))  # ['apple', 'banana', 'orange']

# Alignment and padding
print("cat".center(10, "-"))     # '---cat----'
print("42".zfill(5)        )     # '00042'
