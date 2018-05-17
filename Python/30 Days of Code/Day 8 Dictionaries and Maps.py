# Solution for Day 8 Dictionaries and Maps

n = int(input())

di = {}
for i in range(n):
    split = input().split(" ")
    di[split[0]] = split[1]

while True:
    name = input()
    if not name:
        break

    phone = di.get(name)

    if not phone:
        print("Not found")
    else:
        print(name, "=", phone, sep="")
