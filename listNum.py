number = []

for row in range(0,6):
    print(row+1, end="")
    number.append(input("."))

print()

for row in range(0,6):
    print(number[row])