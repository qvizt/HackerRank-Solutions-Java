# Solution for The Captain's Room


if __name__ == '__main__':
    k = int(input())
    li = list(map(int, input().split()))
    rooms = set()
    duplicates = set()

    for room in li:
        if room not in rooms:
            rooms.add(room)
        else:
            duplicates.add(room)

    print(rooms.difference(duplicates).pop())
