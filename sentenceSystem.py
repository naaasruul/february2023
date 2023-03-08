sentences = []

for i in range(0,2):
    userInput = input("enter sentences: ")
    sentences.append(userInput)

print("sentences 1: ", sentences[0])
print("sentences 2: ", sentences[1])

for i in range(len(sentences)):
    print("sentences",i+1,"has: ", len(sentences[i]))

if len(sentences[0]) > len(sentences[1]):
    print("sentences 1 more than sentences 2")
else:
    print("sentences 1 more than sentences 2")
