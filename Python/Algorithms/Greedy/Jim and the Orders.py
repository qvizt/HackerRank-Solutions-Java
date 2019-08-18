# Solution for Jim and the Orders


def get_delivery_sequence(orders):
    orders.sort(key=lambda x: x[1] + x[2])
    sequence = [x[0] for x in orders]
    return sequence


if __name__ == '__main__':
    n = int(input())
    orders = []
    for c in range(n):
        order, time = list(map(int, input().split()))
        orders.append((c + 1, order, time))
    delivery_sequence = get_delivery_sequence(orders)
    print(*delivery_sequence)
