for i in [0,1,2]:
    print(i)
# Range to Create a List
for i in range(3):
    print(i)
# Do not need to use i as variable **********    
for _ in range(3):
    print("Hello!")
# Putting End in print to remove extra line
print("Subhojit\n"*3,end="")    

# How to take input
while True:
    n=int(input("What's N? "))
    if n > 0:
        break

for _ in range(n):
    print("Subhojit!")

# Dictonary ---- ###
Names=["Subhojit","Adwait","Cindy","Pupu"]
Locations=[]    