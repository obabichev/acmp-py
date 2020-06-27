class List:
    def __init__(self, root=None):
        self.root = root

    def append(self, val):
        if self.is_cycle():
            raise AssertionError
        if self.root is None:
            self.root = Node(val)
            return

        current = self.root
        while current.next is not None:
            current = current.next
        current.next = Node(val)

    def is_cycle(self):
        if not self.root or not self.root.next:
            return False
        i = self.root.next.next
        j = self.root.next

        while i != j:
            if i is None or i.next is None:
                return False
            i = i.next.next
            j = j.next
        return True

    def reverse(self):
        if self.is_cycle():
            raise AssertionError
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
        i = 0
        while current is not None and i < 3:
            result.append(current.val)
            current = current.next
            i = i + 1
        return '<List' + ','.join([str(x) for x in result]) + '>'


class Node:
    def __init__(self, val, _next=None):
        self.val = val
        self.next = _next

    def __repr__(self):
        return '<Node ' + str(self.val) + '>'


a = Node(1)
d = Node(5, Node(4, Node(3, Node(3, Node(2, a)))))
a.next = d
e = Node(6, d)
f = Node(7, e)
l = List(f)
print(l)
print('Cycle' if l.is_cycle() else 'Not cycle')
