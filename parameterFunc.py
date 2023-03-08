

def calculation(num1,num2, choice):
    if choice == "1":
        print(num1,"+",num2,"=",num1 + num2)
    if choice == "2":
        print(num1,"-",num2,"=",num1 - num2) 

print("enter 2 numbers: ")
number1 = int(input(">"))
number2 = int(input(">"))

print("""
    Menu
1. ADD
2. MINUS """)
1
userChoice = input("choose an option: ")
calculation(number1,number2,userChoice)

