# Solution for Day 6 Let's Review

t = int(input())

for i in range(t):
    s = input()
    line = s[0::2] + " " + s[1::2]
    print(line)