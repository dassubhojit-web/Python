#This my 1st Python Programme
'''Date is Sunday 25th Jan 2026'''
print("Hello Subhojit!\nHow are you doing today?")
place=input("Where are you now? ").strip().title()
feeling=input("How are you feeling today?\n")
print("Hello Subhojit! You are now in",place,"\nI am feeling",feeling)
print(f"Hello Subhojit you are in {place}")
# Multiple funaction call in a single line
name=input("What is your name? ").strip().title()
# Split function to split by using delimitor
first,last=name.split(" ")
print(f"Your First Name is {first}")