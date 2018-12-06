# Solution for Gemstones

def get_nr_of_gemstones(rocks):
    gemstones = {}

    for r in rocks:
        mineral_set = set()

        for m in r:
            mineral_set.add(m)

        for m in mineral_set:
            count = gemstones.get(m, 0)
            count += 1
            gemstones[m] = count

    nr_gemstones = 0
    for nr in gemstones.values():
        if nr == len(rocks):
            nr_gemstones += 1

    return nr_gemstones


if __name__ == '__main__':
    n = int(input())
    rocks = []

    for _ in range(n):
        rocks.append(input())

    result = get_nr_of_gemstones(rocks)

    print(result)
