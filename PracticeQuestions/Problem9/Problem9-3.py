# Write a program to generate multiplication tables from 2 to 20 and write it to the different files. Place these files in a folder for a 13 – year old.

# Function to display the table in different files.
def multiplication_table(num):
    times_table = ''

    for i in range(1, 10 + 1):
        times_table += f"{num} X {i} = {num * i}\n"

    filename = f"PracticeQuestions/Problem9/TimesTable/times_table{num}.txt"
    with open(filename, 'w') as f:
        f.write(times_table)    

# Loop that iterates the numbers from 2 to 20
for i in range(2, 20 + 1):
    multiplication_table(i)