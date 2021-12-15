def explore(grid, location, visited):
    r, c = location
    rowcheck = 0 <= r < len(grid)
    colcheck = 0 <= c < len(grid[0])

    if not(rowcheck and colcheck): return False
    if grid[r][c] == 0: return False
    if location in visited: return False

    visited.add(location)

    explore(grid, (r-1, c), visited)
    explore(grid, (r+1, c), visited)
    explore(grid, (r, c-1), visited)
    explore(grid, (r, c+1), visited)
    return True


def islandCount():
    inp_arr = [
        [0, 1, 0, 0, 1, 0],
        [1, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0],
        [0, 1, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0],
    ]

    visited = set()
    ctr = 0
    for i in range(len(inp_arr)):
        for j in range(len(inp_arr[0])):
            if (i, j) not in visited:
                if explore(inp_arr, (i, j), visited):
                    ctr += 1
    return ctr

print(islandCount())

