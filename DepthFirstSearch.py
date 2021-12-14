class DepthFirstSearch:
    def __init__(self):
        self.root = None

    def gridtoadjlist(self, graph):
        out_graph = {}
        for k, v in graph:
            if k not in out_graph:
                out_graph[k] = []
            if v not in out_graph:
                out_graph[v] = []
            out_graph[k].append(v)
            out_graph[v].append(k)
        return out_graph


    def haspathcyclic(self, graph, start, end, check = None):
        if start == end: return True
        if check is None:
            check = set()

        if start in check:
            return False

        check.add(start)

        for v in graph[start]:
            if self.haspath(graph, v, end, check) == True:
                return True

        return False

    def largestIsland(self, graph):
        visited = set()
        max_val = 0

        for k in graph.keys():
            if k not in visited:
                max_val = max(max_val, self.get_size(graph, k, visited))

        return max_val

    def get_size(self, graph, curr, visited):
        if curr in visited: return 1
        visited.add(curr)
        ctr = 1

        for val in graph[curr]:
            ctr += self.get_size(graph, curr, visited)

        return ctr

    def connectedcomponents(self, graph):
        visited = set()
        ctr = 0

        for k in graph.keys():
            if self.explore(graph, k, visited):
                ctr+=1
        return ctr

    def explore(self, graph, curr, visited):
        if curr in visited: return False

        visited.add(curr)
        for v in graph[curr]:
            self.explore(graph, v, visited)

        return True


    # Only works for acyclic graphs
    def haspath(self, graph, start, end):
        if start == end: return True

        for v in graph[start]:
            if self.haspath(graph, v, end) == True:
                return True

        return False

    # Only works for acyclic graphs
    def display(self, graph, start):
        stack = [start]

        while len(stack) > 0:
            val = stack.pop()
            print(val)

            for v in graph[val]:
                stack.append(v)

    # Only works for acyclic graphs
    def _display(self, graph, start):
        print(start)
        for val in graph[start]:
            self._display(graph, val)



if __name__ == '__main__':
    dfs = DepthFirstSearch()
    # d = {
    #     'f': ['g', 'i'],
    #     'g': ['h'],
    #     'h': [],
    #     'i': ['g', 'k'],
    #     'j': ['i'],
    #     'k': []
    # }

    # edges = [['i', 'j'], ['k', 'i'], ['m', 'k'], ['k', 'l'], ['o', 'n']]

    graph = {
        0: [8, 1, 5],
        1: [0],
        5: [0, 8],
        8: [0, 5],
        2: [3, 4],
        3: [2, 4],
        4: [3, 2]
    }

    # graph = dfs.gridtoadjlist(edges)
    # print(graph)

    # print(dfs.connectedcomponents(graph))
    print(dfs.largestIsland(graph))
    # dfs.display(graph, 'i')