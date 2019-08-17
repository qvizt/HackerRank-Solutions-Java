# Solution for Priyanka and Toys


def get_number_of_containers(weights):
    weights.sort()
    nr_containers = 1
    current_weight_limit = weights[0] + 4

    for i in range(1, len(weights)):
        w = weights[i]
        if w > current_weight_limit:
            current_weight_limit = w + 4
            nr_containers += 1

    return nr_containers


if __name__ == '__main__':
    input()  # skip n
    weights = list(map(int, input().split()))
    nr_containers = get_number_of_containers(weights)
    print(nr_containers)
