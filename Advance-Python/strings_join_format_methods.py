# join() method ==> Used to join a list (or any iterable) of strings into a single string with a separator.

# Syntax: 'separator'.join(iterable)
# separator → string to insert between each element.
# iterable → a list, tuple, or other iterable of strings only.

names = ["Rohan", "Kamal", "Thakur"]

joined_str = ' and '.join(names)

print(joined_str)

# This will raise an error
# print(' '.join([1, 2, 3]))  
# TypeError: sequence item 0: expected str instance, int found

print(' '.join(map(str, [1, 2, 3])))  # "1 2 3"


# format() method ==> Used to inject values into a string templates using placeholders {}

# Syntax: 'template string {}'.format(value)

print("Hello, {}".format("World"))

print("I have {} apples and {} oranges.".format(12, 9))

# Positional Indexing 
# Hello Bob, meet Alice
print("Hell0 {1}, meet {0}". format("Alice", "Bob"))

# Hello Alice, meet Bob
print("Hell0 {0}, meet {1}". format("Alice", "Bob"))

# Named placeholders
print("Name: {name}, Age: {age}".format(name="Rohan", age=22))


# Combining with join()
items = ['milk', 'bread', 'butter']
print(", ".join("Item: {}".format(item) for item in items))