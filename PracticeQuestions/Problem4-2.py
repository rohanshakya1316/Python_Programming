# Write a program to accept marks of 6 students and display them in a sorted manner. 

marks = [] 

m1 = int(input('Enter marks of student 1: '))
marks.append(m1)
m2 = int(input('Enter marks of student 2: '))
marks.append(m2)
m3 = int(input('Enter marks of student 3: '))
marks.append(m3)
m4 = int(input('Enter marks of student 4: '))
marks.append(m4)
m5 = int(input('Enter marks of student 5: '))
marks.append(m5)
m6 = int(input('Enter marks of student 6: '))
marks.append(m6)

marks.sort()

print(marks)

# Alternatives 

scores = []

print("\nEnter scores of students here.")

for i in range(1, 7):
    score = int(input(f"Enter marks of student {i}: "))
    scores.append(score) 

scores.sort()

print("\nThe marks of students in sorted order are: ")

print(scores)