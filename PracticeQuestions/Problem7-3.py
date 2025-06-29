# Write a program to find whether a given number is prime or not. 

num = int(input("Enter any number: "))

for i in range(2, num):
    if num % i == 0:
        print(f"{num} is not prime number.")
        break
else:
    print(f"{num} is a prime number.")

# Alternatives

if num <= 1:
    print(f"{num} is not a prime number.")
else:
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(f"{num} is a prime number.")
    else: 
        print(f"{num} is not a prime number.")