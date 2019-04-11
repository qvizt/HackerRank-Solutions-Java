# Solution for Ice Cream Parlor
#
# NOTE: This is not a solution based on "Binary Search"

def get_flavors(money, cost_flavors):
    result = []
    cost_flavor_mapping = {}

    for i in range(len(cost_flavors)):
        flavor = i + 1
        cost = cost_flavors[i]
        flavors = cost_flavor_mapping.get(cost, [])
        flavors.append(flavor)
        cost_flavor_mapping[cost] = flavors

    for cost in cost_flavor_mapping.keys():
        difference = money - cost
        flavors = cost_flavor_mapping.get(difference, None)

        if flavors is None:
            continue
        else:
            sunnys_flavor = cost_flavor_mapping[cost][0]
            if cost == difference:
                if len(flavors) == 1:
                    continue
                else:
                    johnnys_flavor = flavors[1]
            else:
                johnnys_flavor = flavors[0]
            result.append(sunnys_flavor)
            result.append(johnnys_flavor)
            result.sort()
            break

    return ' '.join([str(x) for x in result])


if __name__ == '__main__':
    tests = int(input())

    for _ in range(tests):
        money = int(input())
        input()  # skip number of flavors
        cost_flavor_list = [int(x) for x in input().split()]
        flavors = get_flavors(money, cost_flavor_list)

        print(flavors)
