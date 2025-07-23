# Store the multiplication tables generated in problem 3 in a file name Tables.txt

import Problem12_3 as p12_3

table = p12_3.table_comprehensed

n = p12_3.mul_num

with open("./PracticeQuestions/Problem12/Tables.txt", 'a') as tb:
    content = f"Table of {n}: " + " ".join(str(x) for x in table) + "\n"
    tb.write(content)