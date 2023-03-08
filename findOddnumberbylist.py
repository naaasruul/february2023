value = [10,33,20,23,56,21,52,31]
oddNum = []
sum = 0

print("odd number")

for i in value:
    if i % 2 == 1:
        oddNum.append(i)
        sum = sum + i
        average = sum/len(oddNum)

# print(oddNum)
for i in range(len(oddNum)):
    print(">",oddNum[i])

# print sum
print("sum =",sum)

# print average
print("average =",average)
