studentName = input("enter name: ")
sum = 0
i = 0
choice = "y"

while choice == "y":
    for i in range(5):
        mark = int(input("enter your mark: "))
        sum = sum + mark
        i = i + 1
    print(studentName, "mark total is: ",sum)
    choice = input("do you want to continue? y/n: ")
else:
    print("thank you")
    break

# kalau jodoh tak ke mana adinda 

        