# The match statement is used to perform different actions based on different conditions.

month = int(input("Enter the month number: "))
day = int(input("Enter the day number: "))

match day:

    case 1:
        print("Sunday")

    case 2:
        print("Monday")

    case 3:
        print("Tuesday")

    case 4:
        print("Wednesday")

    case 5:
        print("Thursday")

    case 6:
        print("Friday")

    case 7:
        print("Saturday")
    
    # The value _ will always match, so it is important to place it as the last case to make it behave as a default case.
    case _:         # Default case
        print("Invalid day number!")


# Combine Values
# Use the pipe character | as an or operator in the case evaluation to check for more than one value match in one case
match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Today is a weekday.")
    
    case 6 | 7:
        print("Today is weekends.")

    case _:
        print("Invalid!")

# We can add if statements in the case evaluation as na extra condition - check
match day: 
    case 1 | 2 | 3 | 4 | 5 if month == 4:
        print("A weekday in April")

    case 1 | 2 | 3 | 4 | 5 if month == 5:
        print("A weekday in May")
        
    case _:
        print("No match")
