# Solution for Day 20 Sorting

# !/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here

swaps = 0

for i in range(n):
    swaps_snapshot = swaps

    for j in range(n - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            swaps += 1

    if swaps == swaps_snapshot:
        break

print("Array is sorted in", swaps, "swaps.")
print("First Element:", a[0])
print("Last Element:", a[n - 1])
