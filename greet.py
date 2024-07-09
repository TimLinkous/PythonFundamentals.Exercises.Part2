def greet(name):
    print("Hello, welcome to ZipCode", name,"!")

#greet("Tim")
#greet("Darth Vader")
#greet("Guido Van Rossum")

def name_input():
    name = input("Please enter your name.\n")
    return name
    
greet(name_input())