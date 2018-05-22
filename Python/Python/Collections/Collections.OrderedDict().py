# Solution for Collections.OrderedDict()

from collections import OrderedDict

if __name__ == '__main__':
    ordered_dictionary = OrderedDict()

    n = int(input())

    for i in range(n):
        data = input().split()
        item_name = str(" ".join(data[0:len(data) - 1]))
        net_price = int(data[len(data) - 1])

        if ordered_dictionary.get(item_name):
            ordered_dictionary[item_name] += net_price
        else:
            ordered_dictionary[item_name] = net_price

    for k, v in ordered_dictionary.items():
        print(k, v)
