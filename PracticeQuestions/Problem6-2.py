# Write a program to find out whether a student has passed or failed if it requires a total of 40 % and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input fromthe user.

sub1_marks = float(input("Enter the marks of first subject: "))
sub2_marks = float(input("Enter the marks of second subject: "))
sub3_marks = float(input("Enter the marks of third subject: "))

total_percent = ((sub1_marks + sub2_marks + sub3_marks) / 300) * 100

if total_percent >= 40 and sub1_marks >= 33 and sub2_marks >= 33 and sub3_marks >= 33:
    print("You are passed. Your percentage is", total_percent)

else:
    print("You are failed. Your percentage is", total_percent)