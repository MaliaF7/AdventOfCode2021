#PART ONE
from collections import Counter
with open("day3Input.txt", "r") as f:
    numbers = list(map(lambda x: x.strip(), f.readlines()))

gamma =''
epsilon=''

                    
for i in range(len(numbers[0])): 
    x = ''
    for j in numbers:
        x += j[i]

    gamma += Counter(x).most_common()[0][0]
    epsilon += Counter(x).most_common()[1][0]

print(int(gamma, 2) * int(epsilon, 2))

#PART TWO
from collections import Counter

numbers = [n for n in open("day3Input.txt").read().strip().split("\n")]
oxygenNums = numbers[:]
co2Nums = numbers[:]

for i in range(len(numbers[0])):
    oxygenCount = Counter([n[i] for n in oxygenNums])
    co2Count = Counter([n[i] for n in co2Nums])

    if len(oxygenNums) > 1:
        if oxygenCount["0"] > oxygenCount["1"]:
            oxygenNums = [n for n in oxygenNums if n[i] == "0"]
        else:
            oxygenNums = [n for n in oxygenNums if n[i] == "1"]

    if len(co2Nums) > 1:
        if co2Count["0"] > co2Count["1"]:
            co2Nums = [n for n in co2Nums if n[i] == "1"]
        else:
            co2Nums = [n for n in co2Nums if n[i] == "0"]

print(int(oxygenNums[0], 2) * int(co2Nums[0], 2))
