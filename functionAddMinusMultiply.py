print("""
- Menu -
1 ADD
2 MINUS
3 MULTIPLY
""")

def add():
    list = []
    sum = 0
    for i  in range(0,6):
        userNum = int(input("enter number: "))
        list.append(userNum)
        sum = sum + userNum

    print("total sum is ",sum)

def minus():
    list = []
    sum = 0
    for i  in range(0,6):
        userNum = int(input("enter number: "))
        addNum = list.append(userNum)
        sum = sum - userNum

    print("total is ",sum)

def multiply():
    list = []
    sum = 0
    for i  in range(0,6):
        userNum = int(input("enter number: "))
        addNum = list.append(userNum)
        sum = sum * userNum

    print("total is ",sum)
    



userChoose = int(input("choose operation: "))

if userChoose == 1:
    add()
elif userChoose == 2:
    minus()
elif userChoose == 3:
    multiply()
else:
    print("its not an option!!")

