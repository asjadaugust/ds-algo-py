

def calcMinDist(graph):
    arr = []
    for i, x in enumerate(graph):
        _min = float('inf')
        for j, y in enumerate(graph):
            if y:
                _min = min(_min, abs(j-i))
        arr.append(_min)
    return arr



blocks = [
    {
        "gym": False,
        "school": True,
        "store": False
    },
    {
        "gym": True,
        "school": False,
        "store": False
    },
    {
        "gym": True,
        "school": True,
        "store": False
    },
    {
        "gym": False,
        "school": True,
        "store": False
    },
    {
        "gym": False,
        "school": True,
        "store": True
    }
]

arr = []
for k in blocks[0].keys():
    arr.append(calcMinDist([x[k] for x in blocks]))

_min_arr = []
_min = float('inf')
for res in map(list, zip(*arr)):
    _min_arr.append(max(res))

print(_min_arr.index(min(_min_arr)))