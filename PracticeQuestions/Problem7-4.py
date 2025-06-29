# Write a program to find the sum of first n natural numbers using while loop.

n = int(input("Enter a number upto where you want to find the sum: "))

sum = 0

# using for loop
for i in range(n + 1):
    sum += i
print(f"The sum of first {n} natural number is {sum}.")

# using while loop
sum = 0
while n > 0:
    sum += n
    n -= 1
print(f"The sum of first {n} natural number is {sum}.")
