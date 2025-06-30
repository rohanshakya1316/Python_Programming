# Write a recursive function to calculate the sum of first n natural numbers.

def sum_of_natural_number(n):
    if n == 1: 
        return 1
    else:
        return n + sum_of_natural_number(n - 1)


number = int(input("Enter a number upto where you want to find sum: "))

aggregrate = sum_of_natural_number(number)

print(f"The sum of first {number} is {aggregrate}.")