# Solution for Marc's Cakewalk


def get_miles_to_walk(calories):
    calories.sort(reverse=True)
    miles = 0
    for i in range(len(calories)):
        miles += pow(2, i) * calories[i]

    return miles


if __name__ == '__main__':
    input()  # skip n
    calories = list(map(int, input().split()))
    miles = get_miles_to_walk(calories)
    print(miles)
