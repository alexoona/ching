
from collections import deque

def bfs(start, goal):
    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path

        stacks = [list(s) for s in state]

        for i in range(len(stacks)):
            if not stacks[i]:
                continue

            block = stacks[i][-1]

            for j in range(len(stacks) + 1):
                if i == j:
                    continue

                new_stacks = [s[:] for s in stacks]
                new_stacks[i].pop()

                if j == len(stacks):
                    new_stacks.append([block])
                else:
                    new_stacks[j].append(block)

                new_state = tuple(
                    tuple(s) for s in new_stacks if s
                )

                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, path + [new_state]))

    return None

def print_state(state):
    for i, stack in enumerate(state):
        print("Stack", i + 1, ":", list(stack))
    print()

start = (('C', 'B', 'A'),)
goal = (('A', 'B', 'C'),)

solution = bfs(start, goal)

if solution:
    print("Solution Found!")
    for step, state in enumerate(solution):
        print("Step", step)
        print_state(state)
else:
    print("No Solution Found")
