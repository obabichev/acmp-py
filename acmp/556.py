def lines():
    with open('../INPUT.TXT', "r") as f:
        return f.readlines()


memo = dict()


def mult(v1, v2):
    return v1[0] * v2[0] + v1[1] * v2[1], v1[1] * v2[0] + v1[0] * v2[1]


def solution(n, arr):
    curr = (1, 0)
    for p in arr:
        curr = mult(curr, (p, 1 - p))
    return "{:.6f}".format(curr[0])


def read():
    l = lines()
    n = int(l[0])
    arr = [float(x) for x in l[1].split(' ')]
    return n, arr


_in = read()
print (solution(_in[0], _in[1]))

assert solution(3, [1, 0.1, 0.9]) == 0.18
# assert solution(6) == 2
