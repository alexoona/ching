n = int(input("Enter number of disks: "))

start = tuple([0] * n)
goal = tuple([2] * n)

queue = [(start, [])]
visited = [start]

while queue:
    state, path = queue.pop(0)

    if state == goal:
        print("Minimum moves:", len(path))
        for move in path:
            print(move)
        break

    pegs = [[], [], []]

    for disk in range(n):
        pegs[state[disk]].append(disk)

    for i in range(3):
        if pegs[i]:
            disk = pegs[i][0]

            for j in range(3):
                if i != j and (not pegs[j] or pegs[j][0] > disk):
                    new_state = list(state)
                    new_state[disk] = j
                    new_state = tuple(new_state)

                    if new_state not in visited:
                        visited.append(new_state)
                        print(new_state)
                        new_path = path + [(i, j, disk + 1)]
                        queue.append((new_state, new_path))







