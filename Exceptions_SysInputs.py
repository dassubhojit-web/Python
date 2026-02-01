import sys
import cowsay

if len(sys.argv) == 1:
    sys.exit("Please provide your name!")
elif len(sys.argv) > 2:
    sys.exit("You provided too many args")
else:
    name=sys.argv[1]
    while True:
        try:
            age=int(input("What Your Age?"))
        except:
            print("It is not a number!")
        else:
            print(f"{name}'s age is {age}")
            break
namelst=["No Name","Subhojit","Sonali","Adwait","Dipak"]
print(namelst[1:])
for lstname in namelst[1:]:
    print(lstname)

cowsay.say("Hello!")    