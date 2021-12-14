def islandCount():
    inp_arr = [
        [0, 1, 0, 0, 1, 0],
        [1, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0],
        [0, 1, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0],
    ]

    r, c = len(inp_arr), len(inp_arr[0])

    for i in range(r):
        for j in range(c):
            print()

islandCount()

