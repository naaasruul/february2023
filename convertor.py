

while True:
    print("""
                Welcome!
-------------------------------------------
               MENU                       | 
1. gm to kg                               |   
2. miles to kilometer                     |
3. RM to USD                              |
4. Exit                                   |
-------------------------------------------
""")
    conversion = int(input("choose conversion: "))


    # if user choose 1, convert g to kg
    if conversion == 1:
        gramInput = int(input("Enter grams: "))
        kilogram = gramInput / 1000
        print("Kilograms = ", round(kilogram,2))


# if user choose 2, convert miles to USD
    elif conversion == 2:
        milesInput = int(input("Enter miles: "))
        kilometer = milesInput * 1600
        print("kilometers = ", round(kilometer, 2))


    # if user choose 3, convert RM to USD
    elif conversion == 3:
        ringgitInput = int(input("Enter Ringgit: "))
        usd = ringgitInput * 0.23
        
        print("USD = ", round(usd,2))


    # user want to exit
    elif conversion == 4:
        print("Thank you !")
        break
    
    # user enter wrong option
    else:
        print("there is no option for your number!!!")


    # 
    retry = input("do you want to proceed? y/n: ")
    if retry == "n":
        print("Thank you!!")
        break

        



