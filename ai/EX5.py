grid = [
    ['S', '.', '.'],
    ['X', '.', '.'],
    ['.', '.', 'G']
]

def bfs():
    queue = [[(0, 0)]]          
    visited = [(0, 0)]

    while queue:
        path = queue.pop(0)     
        row, col = path[-1]     

        if grid[row][col] == 'G':
            return path


        for r, c in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row = row + r
            new_col = col + c


            if new_row < 0 or new_row > 2 or new_col < 0 or new_col > 2:
                continue


            if grid[new_row][new_col] == 'X':
                continue
            if (new_row, new_col) in visited:
                continue

            visited.append((new_row, new_col))
            queue.append(path + [(new_row, new_col)]) 

    return None

path = bfs()

if path:
    print("Path Found:")
    for position in path:
        print(position)
    print("Minimum Steps:", len(path) - 1)
else:
    print("No Path Found")
