#Part One

with open("File1.txt", "r") as f:
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
print(f"Part 1: {h=} and {d=} ==> {h*d}")



