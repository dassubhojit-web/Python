'''This is Simple Calculator Python Code;It's take 2 Number and Calculate Sum/Subtract/Multiplication/Division'''

def main():
    a=float(input("Please Enter Your Frist Number:\t\t").strip())
    b=float(input("Please Enter Your Second Number:\t").strip())
    print(f"You have entered two numbers as {a},{b}\nPlease let me know which arithmatics operation you want to perform.\nYour options are\n\t1.Sum\n\t2.Subtraction\n\t3.Multiplication\n\t4.Division")
    option=int(input("Please Select Number from the above\t").strip())
    if option == '':
        banner="You have not chossen any option"
    elif option == 1:
        banner="Summation"
    elif option == 2:
        banner="Subtraction"
    elif option == 3:
        banner="Multiplication"
    elif option == 4:
        banner="Division"    
    print(f"You have choosen option: {option} {banner}")
    if option == 1:
        op=Summation(a,b)
    elif option == 2:
        op=Subtraction(a,b)
    elif option == 3:
        op=Multiplication(a,b)
    elif option == 4:
        op=Division(a,b)
    else:
        op=0 
    print(f"Your output {op}")

def Summation(x,y):
    return(x+y)

def Subtraction(x,y):
    return(x-y)

def Multiplication(x,y):
    return(x*y)

def Division(x,y):
    return(x/y)

main()