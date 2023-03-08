name = input("Enter your name: ")
sum = 0


for i in range(1,11):
        print("enter your mark", i,":")
        mark = int(input("your mark -> "))
        sum = sum + mark

print("hi!", name)
        
if sum < 40:
    print("your fail!")
elif sum < 70:
    print("your almost fail")
else:
    print("congrats")

print("your mark is: ", sum)