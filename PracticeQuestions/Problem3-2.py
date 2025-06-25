# Write a program to fill in a letter template given below with name and date. 
# letter = ''' 
            # Dear < |Name|>, 
            # You are selected! 
            # <|Date|> 
            # '''


name = input("Enter your name: ") 

date = input("Enter date: ") 

letter = f"""'''Dear {name}
             You are selected! 
             {date}
             '''"""

print(letter)

# Alternative 
string = ''' 
Dear < |Name| >, 
You are selected! 
< |Date| > 
'''

print(string.replace("< |Name| >", "Rohan").replace('< |Date| >', '2025/08/12'))