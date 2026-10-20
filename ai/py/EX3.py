
import heapq

goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
start = (1, 2, 3, 4, 0, 6, 7, 5, 8)

def heuristic(state):
    distance = 0
    for i in range(9):
        if state[i] != 0:
            goal_pos = goal.index(state[i])
            distance += abs(i // 3 - goal_pos // 3)
            distance += abs(i % 3 - goal_pos % 3)
    return distance

def neighbours(state):
    result = []
    blank = state.index(0)
    row, col = divmod(blank, 3)

    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        r, c = row + dr, col + dc

        if 0 <= r < 3 and 0 <= c < 3:
            pos = r * 3 + c
            new_state = list(state)
            new_state[blank], new_state[pos] = new_state[pos], new_state[blank]
            result.append(tuple(new_state))

    return result

def a_star(start):
    queue = [(heuristic(start), 0, start)]
    parent = {start: None}
    cost = {start: 0}

    while queue:
        f, g, current = heapq.heappop(queue)

        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()

            for i, state in enumerate(path):
                print("Move", i)
                print(state[:3])
                print(state[3:6])
                print(state[6:])
                print()

            print("Total Moves =", len(path) - 1)
            return

        for child in neighbours(current):
            new_g = g + 1

            if child not in cost or new_g < cost[child]:
                cost[child] = new_g
                parent[child] = current
                heapq.heappush(
                    queue,
                    (new_g + heuristic(child), new_g, child)
                )

    print("No Solution Found")

a_star(start)
