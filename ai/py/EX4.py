
from collections import deque

n = int(input("Enter number of disks: "))

start = tuple([0] * n)
goal = tuple([2] * n)

queue = deque([(start, [])])
visited = {start}

while queue:
    state, path = queue.popleft()

    if state == goal:
        print("Minimum moves:", len(path))
        for move in path:
            print(move)
        break

    pegs = [[], [], []]

    for disk, peg in enumerate(state):
        pegs[peg].append(disk)

    for i in range(3):
        if not pegs[i]:
            continue

        disk = pegs[i][0]

        for j in range(3):
            if i != j and (not pegs[j] or pegs[j][0] > disk):
                new_state = list(state)
                new_state[disk] = j
                new_state = tuple(new_state)

                if new_state not in visited:
                    visited.add(new_state)
                    queue.append(
                        (new_state, path + [(i, j, disk + 1)])
                    )
