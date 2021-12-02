#Part One of the Challenge

with open('input.txt', 'r') as f:
myInputs = f.readlines()
depth = 0

for i in range(1, len(myInputs)):
    if int(myInputs[i]) > int(myInputs[i-1]):
        depth += 1

print(depth)


#Part two of the challenge

with open('input.txt', 'r') as f:
    myInput = f.readlines()
myInput = [int(i) for i in myInput]
count = 0
curentNum=0
nextNum = 0
for i in range(len(myInput)-3):
    currentNum = myInput[i]+myInput[i+1]+myInput[i+2]
    nextNum = myInputi+1]+myInput[i+2]+myInput[i+3]
    if nextNum > currentNum:
        count += 1
print(count)
