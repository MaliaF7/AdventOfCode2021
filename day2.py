#PART TWO
with open("input.txt", "r") as f:
    data=f.readlines()
h = d = 0
for move in data:
    direction, amount = move.split(" ")
    if direction == "forward":
        h += int(amount)
    elif direction == "down":
        d += int(amount)
    else:
        d -= int(amount)
print(h*d)


#PART TWO
with open("input.txt", "r") as f:
    data=f.readlines()
h = d = a = 0
for move in data:
    direction, amount = move.split(" ")
    if direction == "forward":
        h += int(amount)
        d += int(amount) * a
    elif direction == "down":
        a += int(amount)
    else:
        a -= int(amount)
print(h*d)

