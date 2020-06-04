def matrix(n):
    return [[0 for x in range(n)] for y in range(n)]


def solution(n, k, field):
    def get_ways_amount(prev, i, j):
        if i < 0 or j < 0 or i >= n or j >= n:
            return 0
        if field[i][j] == 1:
            return 0
        return prev[i][j]

    next = matrix(n)
    next[0][0] = 1
    for step in range(k):
        prev = next
        next = matrix(n)

        for i in range(n):
            for j in range(n):
                if field[i][j] == 1:
                    continue

                next[i][j] += get_ways_amount(prev, i - 1, j)
                next[i][j] += get_ways_amount(prev, i + 1, j)
                next[i][j] += get_ways_amount(prev, i, j - 1)
                next[i][j] += get_ways_amount(prev, i, j + 1)

        # print(next)
    return next[n - 1][n - 1]


first = input().split()
n = int(first[0])
k = int(first[1])
field = []
for i in range(n):
    field.append([int(x) for x in input()])

print(solution(n, k, field))

# assert solution(3, 6, [[0, 0, 0], [1, 0, 1], [1, 0, 0]]) == 5
