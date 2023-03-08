while True:
    print("Welcome to my budget!")

    month = input("Enter Month: ")

    salary = int(input("enter salary: "))
    otherIncome = int(input("enter other income: "))
    grossIncome = salary + otherIncome

    print("INCOME")
    print("Salary: ", salary)
    print("other income: ", otherIncome)

    print("gross income: ", grossIncome)

    print("Expenses")
    houseRent = int(input("Enter house rent: "))
    carRent = int(input("Enter car rent: "))
    grocery = int(input("Enter grocery: "))
    bill = int(input("Enter electric and water bill: "))
    otherExpenses = int(input("Enter other expenses rent: "))

    totalExpenses = houseRent + carRent + grocery + bill + otherExpenses
    print("total expenses: ", totalExpenses)

    netIncome = grossIncome - totalExpenses
    print("Net income: ", netIncome)

    print("")

    reminder =""
    if netIncome <500:
        reminder = "Youre in danger"
    elif netIncome<2000:
        reminder = "you need to careful"
    else:
        reminder = "you can start saving now"

    print()
    retry = input("check next month? y/n")
    if retry == "n":
        break