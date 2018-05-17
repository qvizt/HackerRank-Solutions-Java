# Solution for Day 2 Operators

# !/bin/python3

import sys

if __name__ == "__main__":
    meal_cost = float(input().strip())
    tip_percent = int(input().strip())
    tax_percent = int(input().strip())

    tip = meal_cost * tip_percent / 100
    tax = meal_cost * tax_percent / 100
    total_cost = meal_cost + tip + tax

    print("The total meal cost is", round(total_cost), "dollars.")