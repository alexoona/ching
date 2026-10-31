grid = [
    ['S', '.', '.'],
    ['X', '.', '.'],
    ['.', '.', 'G']
]

row = 0
col = 0
visited = []

while True:
    visited.append((row, col))
    print("Current Position:", (row, col))

    if grid[row][col] == 'G':
        print("Goal Reached!")
        break

    if col < 2 and grid[row][col + 1] != 'X' and (row, col + 1) not in visited:
        col += 1
    elif row < 2 and grid[row + 1][col] != 'X' and (row + 1, col) not in visited:
        row += 1
    elif col > 0 and grid[row][col - 1] != 'X' and (row, col - 1) not in visited:
        col -= 1
    elif row > 0 and grid[row - 1][col] != 'X' and (row - 1, col) not in visited:
        row -= 1
    else:
        print("No Path Found!")
        break

print("Visited Cells:", visited)