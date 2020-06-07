future = {1}


def solution(n):
    for i in range(0, n - 1):  # 10000
        next = min(future)  # % * 10000
        future.remove(next)
        future.add(next * 2)
        future.add(next * 3)
        future.add(next * 5)
    return min(future)


result = solution(int(input()))
print(result)

# class MinHeap:
#
#     def __init__(self):
#         self.heap = []
#
#     @staticmethod
#     def parent(i):
#         # 1,2 -> 0
#         # 3,4 -> 1
#         # 5,6 -> 2
#         return (i - 1) // 2
#
#     @staticmethod
#     def left(i):
#         # 0 -> 1
#         # 1 -> 3
#         # 2 -> 5
#         return (i * 2) + 1
#
#     @staticmethod
#     def right(i):
#         # 0 -> 2
#         # 1 -> 4
#         # 2 -> 6
#         return (i * 2) + 2
#
#     def swap(self, i, j):
#         tmp = self.heap[i]
#         self.heap[i] = self.heap[j]
#         self.heap[j] = tmp
#
#     def insert(self, value):
#         self.heap.append(value)
#         index = len(self.heap) - 1
#
#         while index > 0 and self.heap[self.parent(index)] > self.heap[index]:
#             self.swap(index, self.parent(index))
#             index = self.parent(index)
#
#     def heapify(self, i):
#         if self.left(i) < len(self.heap) and self.heap[self.left(i)] < self.heap[i]:
#             self.swap(i, self.left(i))
#             self.heapify(self.left(i))
#         elif self.right(i) < len(self.heap) and self.heap[self.right(i)] < self.heap[i]:
#             self.swap(i, self.right(i))
#             self.heapify(self.right(i))
#
#     def pop(self):
#         result = self.heap[0]
#         self.swap(0, -1)
#         del self.heap[-1]
#         self.heapify(0)
#         return result
#
# heap = MinHeap()
#
# def solution(n):


# heap = MinHeap()
#
# heap.insert(4)
# heap.insert(2)
# heap.insert(6)
# heap.insert(1)
# heap.insert(10)
#
# print(heap.heap)
#
# print('pop', heap.pop())
#
# print(heap.heap)
