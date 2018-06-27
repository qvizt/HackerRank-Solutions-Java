# Solution for Electronics Shop


def get_money_spent(b, keyboards, drives):
    keyboards = sorted(keyboards, reverse=True)
    drives = sorted(drives)
    money_spent = -1

    for k in keyboards:
        for d in drives:
            sum_kd = k + d
            if sum_kd > money_spent:
                if sum_kd <= b:
                    money_spent = sum_kd
                else:
                    break

    return money_spent


if __name__ == '__main__':
    b = int(input().split()[0])  # b = budget, n and m are not required
    keyboards = list(map(int, input().split()))
    drives = list(map(int, input().split()))

    money = get_money_spent(b, keyboards, drives)
    print(money)
