'''Define new function'''
#set default value
def hello(to="World"):
    print(f"Hello {to}")

name=input("Please Enter Your Name\t").strip().title()
hello(name)