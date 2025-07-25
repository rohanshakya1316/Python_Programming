class MyClass:
    def __init__(self):
        self.__private_attribute = 42

    def __private_method(self):
        return "This is a private method."

obj = MyClass()

# Attempting to access the mangled name directly
# print(obj.__private_attribute)  # This will raise an AttributeError

# Accessing the mangled name using the mangled form
print(obj._MyClass__private_attribute)

text = obj._MyClass__private_method()
print(text)  # This will print: This is a private method.