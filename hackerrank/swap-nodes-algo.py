class BTree:
    def __init__(self, indexes):
        nodes = [Node(i + 1) for i in range(0, len(indexes))]
        for i in range(0, len(indexes)):
            if indexes[i][0] != -1:
                nodes[i].left = nodes[indexes[i][0] - 1]
            if indexes[i][1] != -1:
                nodes[i].right = nodes[indexes[i][1] - 1]
        self.root = nodes[0]

    def travers(self):
        result = []

        def travers_rec(node):
            if not node:
                return
            travers_rec(node.left)
            result.append(node.value)
            travers_rec(node.right)

        travers_rec(self.root)
        return result


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return '<Node %s>' % self.value


tree = BTree([[2, 3], [4, -1], [5, -1], [6, -1], [7, 8], [-1, 9], [-1, -1], [10, 11], [-1, -1], [-1, -1], [-1, -1]])

print(tree)
print(tree.travers())
