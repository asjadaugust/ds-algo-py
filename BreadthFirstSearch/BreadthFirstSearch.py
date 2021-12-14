from collections import deque

class BreadthFirstSearch:
    def __init__(self) -> None:
        self.root = None

    def haspath(self, graph, start, end):
        queue = deque([start])

        while len(queue) > 0:
            curr = queue.pop()
            if curr == end:
                return True
            for val in graph[curr]:
                queue.appendleft((val))

        return False

    def get_graph(self, edges):
        graph = {}

        for k, v in edges:
            if k not in graph: graph[k] = []
            if v not in graph: graph[v] = []
            graph[k].append(v)
            graph[v].append(k)

        return graph

    def shortest_distance(self, graph, start, end):
        visited = set()
        queue = deque([(start, 0)])

        while len(queue) > 0:
            curr, ctr = queue.pop()
            if curr == end:
                return ctr
            visited.add(curr)

            for val in graph[curr]:
                if val not in visited:
                    queue.appendleft((val, ctr+1))

        return -1


    def display(self, graph, start):
        queue = deque([start])

        while len(queue) > 0:
            curr = queue.pop()
            print(curr)

            for v in graph[curr]:
                queue.appendleft(v)



if __name__ == '__main__':
    dfs = BreadthFirstSearch()
    # d = {
    #     'f': ['g', 'i'],
    #     'g': ['h'],
    #     'h': [],
    #     'i': ['g', 'k'],
    #     'j': ['i'],
    #     'k': []
    # }

    # edges = [
    #     ['w', 'x'], ['x', 'y'], ['z', 'y'], ['z', 'v'], ['w', 'v']
    # ]

    edges = [
        ['a', 'c'], ['a', 'b'], ['c', 'b'], ['c', 'd'], ['b', 'd'], ['e', 'd'], ['g', 'f']
    ]

    graph = dfs.get_graph(edges)
    print(dfs.shortest_distance(graph, 'e', 'c'))
    # print(dfs.haspath(d, 'f', 'k'))
    # dfs.display(d, 'f')