id = []
name = []

for i in range(0,5):
    id.append(input("please enter your ID: "))
    name.append(input("please enter your name: "))

for i in range(0,5):
    print(id[i], name[i])

findId = input("please insert id to find students name: ")

for i in range(0,5):
    if findId == id[i] or findId == name[i]:
        print(id[i],name[i])

        id.pop(i)
        name.pop(i)
        break

print("new list data is: ")
for i in range(0, len(id)):
    print(id[i],name[i])