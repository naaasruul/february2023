marks = []
print("enter your marks:")
for i in range(0,7):
    userMarks = int(input(">"))
    marks.append(userMarks)

print("MARKS LIST")
print(marks)

print(max(marks))
print(min(marks))