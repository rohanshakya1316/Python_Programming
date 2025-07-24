# Lambda is the anonymous function that take any number of arguments, but can only have one expression. 

# Syntax: lambda args : expression 
# (the expression is executed and result is returned.)

args = lambda args : args + 10 
print(args(2))  # prints 12 i.e., 2 + 10 

# Without lambda function 
def square(n):
    print(n * n)

square(5)

# With lambda function 
sq_num = lambda n : n * n
print(sq_num(5))

# Lambda with multiple arguments
mul_num = lambda x, y : x * y
print(mul_num(4, 6))

x = lambda a, b, c : a + b + c
print(x(10, 20, 30))

# Lambda inside a function (closure)
def multiplier(factor):
    return lambda x : x * factor

double = multiplier(2)
print(double(20))

# Lambda with conditional expression 
greatest_num = lambda a, b, c : a if a > b and a > c else b if b > a and b > c else c 
print(greatest_num(12, 23, 34))

# Lambda with data structures 
ordered_pair = [(2, 3), (1, 9), (4, 1), (6, -2)]
# Sort by second element in the pair 
sorted_pair = sorted(ordered_pair)
print(sorted_pair)
sorted_pair = sorted(ordered_pair, key=lambda x : x[1])
print(sorted_pair)

# Nested Lambdas 
nested = lambda x: lambda y : x + y 
add5 = nested(5)
print(add5(100))