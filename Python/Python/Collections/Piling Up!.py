# Solution for Piling Up!

import collections

if __name__ == '__main__':
    t = int(input())

    for i in range(t):
        input()  # nr of cubes not relevant
        cubes = map(int, input().split())
        deque = collections.deque(cubes)

        top = deque.popleft() if deque[0] >= deque[-1] else deque.pop()
        stackable = True

        while deque and stackable:
            if top >= deque[0] >= deque[-1]:
                top = deque.popleft()
            elif deque[-1] <= top:
                top = deque.pop()
            else:
                stackable = False

        if stackable:
            print("Yes")
        else:
            print("No")
