goal  = [1, 2, 3, 4, 5, 6, 7, 8, 0]
start = [1, 2, 3, 4, 0, 6, 7, 5, 8]


def h(state):
    count = 0
    for i in range(9):
        if state[i] != 0 and state[i] != goal[i]:
            count += 1
    return count


def get_children(state):
    b = state.index(0)           
    spots = []

    if b > 2:       spots.append(b - 3)  
    if b < 6:       spots.append(b + 3)   
    if b % 3 != 0:  spots.append(b - 1)   
    if b % 3 != 2:  spots.append(b + 1)   

    children = []
    for s in spots:
        new = state[:]                     
        new[b] = new[s]                    
        new[s] = 0
        children.append(new)
    return children

def a_star():
    open_list = [[h(start), 0, start, [start]]]  
    visited = []

    while len(open_list) > 0:
    
        best = 0
        for i in range(len(open_list)):
            if open_list[i][0] < open_list[best][0]:
                best = i

        f, g, board, path = open_list.pop(best)

        if board == goal:
            print("Solved!")
            for step in path:
                print(step[:3])
                print(step[3:6])
                print(step[6:])
                print()
            print("Total Moves =", len(path) - 1)
            return

        if board in visited:
            continue
        visited.append(board)

        for child in get_children(board):
            if child not in visited:
                new_g = g + 1
                new_f = new_g + h(child)       
                open_list.append([new_f, new_g, child, path + [child]])

    print("No Solution Found")

a_star()
