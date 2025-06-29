# A spam comment is defined as a text containing following keywords: 
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. 
# Write a program to detect these spams. 

spam1 = "Make a lot of money"
spam2 = "buy now"
spam3 = "subscribe this"
spam4 = "click this"

comment = input('Enter your comment: ')

if (spam1 in comment) or (spam2 in comment) or (spam3 in comment) or (spam4 in comment):
    print("The comment is a spam:", comment)

else: 
    print("The comment is not a spam:", comment)

