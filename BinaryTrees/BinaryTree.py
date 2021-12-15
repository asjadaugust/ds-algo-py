from collections import deque

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self) -> None:
        self.root = None

    def dfs_traverse(self, root):
        if not root:
            return []

        out = []
        stack = [root]
        while len(stack) > 0:
            curr = stack.pop()
            out.append(curr.data)

            if curr.right: stack.append(curr.right)
            if curr.left: stack.append(curr.left)

        return out

    def dfs_traverse_rec(self, root):
        if not root:
            return []

        leftVals = self.dfs_traverse_rec(root.left)
        rightVals = self.dfs_traverse_rec(root.right)

        return [root.data, *leftVals, *rightVals]

    def bfs_traverse(self, root):
        if not root: return []
        queue = deque([root])
        out = []

        while len(queue) > 0:
            curr = queue.pop()
            out.append(curr.data)

            if curr.left: queue.appendleft(curr.left)
            if curr.right: queue.appendleft(curr.right)

        return out

    def dfs_search(self, root, value):
        if not root: return False
        if root.data == value: return True

        leftVals = self.dfs_search(root.left, value)
        rightVals = self.dfs_search(root.right, value)
        return leftVals or rightVals

    def bfs_search(self, root, value):
        if not root: return False
        queue = deque([root])

        while len(queue) > 0:
            curr = queue.pop()
            if curr.data == value:
                return True

            if curr.left: queue.appendleft(curr.left)
            if curr.right: queue.appendleft(curr.right)

        return False

    def dfs_tree_sum(self, root):
        if not root: return 0

        leftVals = self.dfs_tree_sum(root.left)
        rightVals = self.dfs_tree_sum(root.right)
        return root.data + leftVals + rightVals

    def bfs_tree_sum(self, root):
        if not root: return 0
        queue = deque([root])
        _sum = 0

        while len(queue) > 0:
            curr = queue.pop()
            _sum += curr.data

            if curr.left: queue.appendleft(curr.left)
            if curr.right: queue.appendleft(curr.right)

        return _sum

    def dfs_tree_min(self, root):
        if not root: return float('inf')

        leftVals = self.dfs_tree_min(root.left)
        rightVals = self.dfs_tree_min(root.right)

        return min(root.data, min(leftVals, rightVals))

    def bfs_tree_min(self, root):
        if not root: return None
        queue = deque([root])
        _min = float('inf')

        while len(queue) > 0:
            curr = queue.pop()
            _min = min(_min, curr.data)

            if curr.left: queue.appendleft(curr.left)
            if curr.right: queue.appendleft(curr.right)

        return _min

    def dfs_max_path_sum(self, root):
        if not root: return float('-inf')
        if not root.right and not root.left: return root.data

        _sum = max(self.dfs_max_path_sum(root.left), self.dfs_max_path_sum(root.right))

        return root.data + _sum

    def invert(self, root):
        self.invert_tree(root)
        return root

    def invert_tree(self, root):
        if not root: return None
        root.left, root.right = root.right, root.left
        self.invert_tree(root.left)
        self.invert_tree(root.right)




a = Node(5)
b = Node(11)
c = Node(3)
d = Node(4)
e = Node(2)
f = Node(1)

a.left = b
b.left = d
b.right = e
a.right = c
c.right = f

bt = BinaryTree()
print(bt.dfs_traverse(a))
print(bt.dfs_traverse((a)))
print(bt.bfs_traverse((a)))
print(bt.bfs_traverse((bt.invert(a))))

print(bt.dfs_search(a, 'g'))
print(bt.bfs_search(a, 'g'))

print(bt.dfs_tree_sum(a))
print(bt.bfs_tree_sum(a))

print(bt.dfs_tree_min(a))
print(bt.bfs_tree_min(a))

print(bt.dfs_max_path_sum(a))