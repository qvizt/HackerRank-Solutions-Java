# Solution for Jumping on the Clouds Revisited


def final_energy(clouds, jump_distance):
    energy = 100

    index = 0
    nr_clouds = len(clouds)

    while True:
        index = (index + jump_distance) % nr_clouds
        current_cloud = clouds[index]

        energy -= 1
        if current_cloud:
            energy -= 2

        if not index:
            break

    return energy


if __name__ == '__main__':
    n, jump_distance = map(int, input().split())
    clouds = list(map(int, input().split()))

    result = final_energy(clouds, jump_distance)
    print(result)
