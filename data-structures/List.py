class List:
    def __init__(self, root=None):
        self.root = root

    def append(self, val):
        if self.root is None:
            self.root = Node(val)
            return

        current = self.root
        while current.next is not None:
            current = current.next
        current.next = Node(val)

    def reverse(self):
        if self.root is None:
            return
        prev = None
        current = self.root

        while current is not None:
            next_ = current.next
            current.next = prev
            prev = current
            current = next_
        self.root = prev

    def __repr__(self):
        current = self.root
        result = []
        while current is not None:
            result.append(current.val)
            current = current.next
        return '<List' + ','.join(result) + '>'


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return '<Node ' + str(self.val) + '>'


l = List()
l.append('1')
l.append('2')
l.append('3')
l.reverse()
print(l)
