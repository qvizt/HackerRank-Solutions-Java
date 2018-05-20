# Solution for Symmetric Difference

if __name__ == "__main__":
    m = int(input())
    m_set = set(map(int, input().split(" ")))

    n = int(input())
    n_set = set(map(int, input().split(" ")))

    set_difference = m_set.symmetric_difference(n_set)

    for val in sorted(set_difference):
        print(val)
