# A program to display the respective grade w.r.t percentage. 

percentage = float(input("Enter your percentage: "))

if percentage < 0 or percentage > 100:
    print("Invalid percentage! Must be between 0 and 100.")

elif percentage >= 90:
    print("Grade: Ex")

elif percentage >= 80:
    print("Grade: A")

elif percentage >= 70:
    print("Grade: B")

elif percentage >= 60:
    print("Grade: C")

elif percentage >= 50:
    print("Grade: D")
    
else:
    print("Grade: F")
