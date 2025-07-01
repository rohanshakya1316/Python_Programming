# Write a python function which converts inches to centimeters. 

def inches_to_cm_converter(inch):
    cm = inch * 2.54    # 1 inch = 2.54cm
    return cm

inchs = float(input("Enter inches to convert to cm: "))

cms = inches_to_cm_converter(inchs)

print(f"{inchs} inches = {cms} cm.")