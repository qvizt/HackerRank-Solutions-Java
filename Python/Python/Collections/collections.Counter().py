# Solution for collections.Counter()

from collections import Counter

if __name__ == '__main__':
    input()  # number of shoes not required
    shoes = Counter(map(int, input().split()))

    earning = 0
    customer_nr = int(input())
    for i in range(customer_nr):
        size, price = map(int, input().split())
        if shoes[size]:
            earning += price
            shoes[size] -= 1

    print(earning)
