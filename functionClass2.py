list = []

for i in range(0,5):
    inputNum = float(input("enter a number: "))
    list.append(inputNum)

minValue = min(list)
maxValue = max(list)

average = round(sum(list) / len(list),2)

print("minimum value: ", minValue)
print("maximum value: ", maxValue)
print("average value: ", average)
