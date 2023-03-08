id = []
name = []

while True:
        for i in range(1,6):
            idInput = id.append(input("enter ID: "))
            nameInput = name.append(input("enter name: "))

        for i in range(0,5):
            print("ID:",id[i],"Student name:", name[i])

        findByid = input("Find by ID: ")

        if findByid == id[0]:
            print(name[0])
        if findByid == id[1]:
            print(name[1])
        if findByid == id[2]:
            print(name[2])
        if findByid == id[3]:
            print(name[3])
        if findByid == id[4]:
            print(name[4])

        removeData = input("remove data: ")

        if removeData == id[0]:
            id.remove(id[0])
            name.remove(name[0])
        if removeData == id[1]:
            id.remove(id[1])
            name.remove(name[1])
        if removeData == id[2]:
            name.remove(name[2])
            id.remove(id[2])
        if removeData == id[3]:
            id.remove(id[3])
            name.remove(name[3])
        if removeData == id[4]:
            id.remove(id[4])
            name.remove(name[4])

        for i in range(0,len(id)):
            print("ID:",id[i],"Student name:", name[i])


retry = input("do you want to continue? y/n: ")