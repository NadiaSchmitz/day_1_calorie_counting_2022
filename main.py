calorie = []
elves = []
sum = 0
max = 0

with open("calorie.txt", "r") as file1:
    for line in file1:
        calorie.append(line)
    print(calorie)

for i in range(0, len(calorie)):
    if calorie[i] != "\n":
        sum = sum + int(calorie[i].replace("\n", ""))
    else:
        elves.append(sum)
        sum = 0

max = sorted(elves)[-1]
print(max)
