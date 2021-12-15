def exploreSum(grid, location, visited):
    r, c = location
    rbound = 0 <= r < len(grid)
    cbound = 0 <= c < len(grid[0])

    if not(rbound and cbound): return 0
    if grid[r][c] == 0: return 0
    if location in visited: return 0

    visited.add(location)
    ctr = 1
    ctr += exploreSum(grid, (r-1, c), visited)
    ctr += exploreSum(grid, (r+1, c), visited)
    ctr += exploreSum(grid, (r, c-1), visited)
    ctr += exploreSum(grid, (r, c+1), visited)

    return ctr


def minIsland(grid):
    _min = float('inf')
    visited = set()
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            size = exploreSum(grid, (r, c), visited)
            if size > 0:
                _min = min(_min, size)
    return _min


grid = inp_arr = [
        [0, 1, 0, 0, 1, 0],
        [1, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0],
        [0, 1, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0],
    ]

print(minIsland(grid))