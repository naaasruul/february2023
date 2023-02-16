student = {}

for i in range(0,3):
    nameInput = input("insert name: ")
    idInput = input("insert ID: ")
    courseInput = input("insert course: ")

    student[i] = {"id":idInput, "name":nameInput, "course":courseInput}




delete = input("please insert id to delete: ")

for i in range(0,3):
    if delete == student[i]["id"]:
        student.pop(i)

print(student)

