# Solution for Mark and Toys


def get_maximum_number_of_items(prices, budget):
    prices.sort()

    current_budget = 0
    nr_items = 0
    for p in prices:
        skip = True
        if (current_budget + p) <= budget:
            current_budget += p
            nr_items += 1
            if current_budget < budget:
                skip = False
                # If the current budget is less than the budget
                # AFTER an item has been added, it is possible that
                # another item can be be added without breaking
                # the budget rule.
        if skip:
            break

    return nr_items


if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    prices = list(list(map(int, input().split())))
    nr_items = get_maximum_number_of_items(prices, k)
    print(nr_items)
