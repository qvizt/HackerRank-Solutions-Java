# Solution for Bon Appetit


def refund(bill, k, b):
    total = sum(bill)
    total -= bill[k]
    ref = b - total // 2

    return ref


if __name__ == '__main__':
    n, k = map(int, input().split())  # n = nr of items, k = item Anna did not eat
    bill = list(map(int, input().split()))
    b = int(input())  # Anna's charge

    ref = refund(bill, k, b)
    if ref:
        print(ref)
    else:
        print("Bon Appetit")
