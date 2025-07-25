# Write a python program to input name, marks and phone number of a student and format it using the format function like: "The name of the student is Rohan, his marks is 88 and phone number is 9989898990"

name = input("Enter your name: ")
marks = float(input("Enter your marks: "))
phone_no = input("Enter your phone number: ")

print("The name of the student is {}, his marks is {} and phone number is {}".format(name, marks, phone_no))