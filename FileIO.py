'''names=[]
for _ in range(3):    
    names.append(input("What is your name? "))

names.sort()
print(names)
'''
name=input("What is your name?\t")
file=open("name.txt","a")
file.write(f"{name} \n")
file.close()

with open("names.txt","a") as file:
    file.write(f"{name} \n",)

with open ("names.txt","r") as file:
    lines=file.readlines()

for line in lines:
    print("hello!",line.rstrip())   

with open ("names.txt","r") as file:
    for line in sorted(file):
       print("hello!",line.rstrip())       