# Solution for Sock Merchant


def total_sock_pairs(socks):
    total_pairs = 0
    pairing = set()
    for s in socks:
        if s in pairing:
            pairing.discard(s)
            total_pairs += 1
        else:
            pairing.add(s)

    return total_pairs


if __name__ == '__main__':
    input()  # n not required
    socks = list(map(int, input().split()))

    result = total_sock_pairs(socks)
    print(result)
