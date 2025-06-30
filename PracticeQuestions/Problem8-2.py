# Write a python program using function to convert Celsius to Fahrenheit and vice versa.

def celsius_to_fahrenheit(deg_c):
    deg_f = (deg_c * 9 / 5) + 32
    return deg_f

def fahrenheit_to_celsius(deg_f):
    deg_c = 5 * (deg_f - 32) / 9
    return deg_c

deg_c = float(input("Enter the temperature in celsius: "))

deg_f = celsius_to_fahrenheit(deg_c)
print(f"The fahrenheit equivalent of {deg_c} is {deg_f}.")


deg_f = float(input("Enter the temperature in fahrenheit: "))

deg_c = fahrenheit_to_celsius(deg_f)
print(f"The celsius equivalent of {deg_f} is {round(deg_c, 2)}.")