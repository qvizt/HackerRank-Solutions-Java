# Solution for Queens Attack II


def count_attacks(length, queen, obstacles):
    attacks = 0
    attacks += _count_attacks_direction(length, queen, obstacles, 0, 1)
    attacks += _count_attacks_direction(length, queen, obstacles, 1, 1)
    attacks += _count_attacks_direction(length, queen, obstacles, 1, 0)
    attacks += _count_attacks_direction(length, queen, obstacles, 1, -1)
    attacks += _count_attacks_direction(length, queen, obstacles, 0, -1)
    attacks += _count_attacks_direction(length, queen, obstacles, -1, -1)
    attacks += _count_attacks_direction(length, queen, obstacles, -1, 0)
    attacks += _count_attacks_direction(length, queen, obstacles, -1, 1)

    return attacks


def _count_attacks_direction(length, queen, obstacles, x_dir, y_dir):
    attacks = 0
    position = queen[0] + x_dir, queen[1] + y_dir
    while 1 <= position[0] <= length and 1 <= position[1] <= length:
        if position not in obstacles:
            attacks += 1
            position = position[0] + x_dir, position[1] + y_dir
        else:
            break
    return attacks


if __name__ == '__main__':
    length, nr_obstacles = map(int, input().split())
    queen = tuple(map(int, input().split()))

    obstacles = set()
    for _ in range(nr_obstacles):
        obstacle = tuple(map(int, input().split()))
        obstacles.add(obstacle)

    result = count_attacks(length, queen, obstacles)
    print(result)
