def solution(n, field):
    d = []

    def from_top(i, j):
        return field[i][j] + d[i - 1][j][0]

    def from_left(i, j):
        return field[i][j] + d[i][j - 1][0]

    for i in range(n):
        d.append([])
        for j in range(0, n):
            if i == 0 and j == 0:
                d[i].append((field[i][j], (-1, -1)))
                continue
            if i == 0:
                d[i].append((from_left(i, j), (i, j - 1)))
                continue
            if j == 0:
                d[i].append((from_top(i, j), (i - 1, j)))
                continue

            top = from_top(i, j)
            left = from_left(i, j)
            if top < left:
                d[i].append((top, (i - 1, j)))
            else:
                d[i].append((left, (i, j - 1)))

    result = [['.' for j in range(n)] for i in range(n)]
    i, j = (n - 1, n - 1)
    while i >= 0 and j >= 0:
        result[i][j] = "#"
        i, j = d[i][j][1]
    return result


n = int(input())
field = []
for i in range(n):
    field.append([int(x) for x in input()])

result = solution(n, field)
print('\n'.join([''.join(line) for line in result]))

# solution(3, [[9, 4, 3],
#              [2, 1, 6],
#              [0, 9, 1]])
