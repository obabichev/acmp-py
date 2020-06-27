def mex(values):
    d = dict()
    for val in values:
        d[val] = True
    current = 0
    while current in d:
        current += 1
    return current


memo = dict()


def g(n, k):
    if n in memo:
        return memo[n]
    if n < k:
        return 0
    if n == k:
        return 1

    values = []
    i = 0
    while i + k <= n:
        values.append(g(i, k) ^ g(n - i - k, k))
        i += 1

    memo[n] = mex(values)
    return memo[n]


def read_integers():
    return [int(x) for x in input().split(' ')]


def read_heaps():
    line = input()
    heaps = []
    _next = False
    current = 0
    for c in line + 'X':
        if c == 'X':
            if current > 0:
                heaps.append(current)
            current = 0
            continue
        current += 1
    return heaps


n, k = read_integers()
heaps = read_heaps()

result = 0
for heap in heaps:
    result = result ^ g(heap, k)

all_less_k = True
for heap in heaps:
    if heap >= k:
        all_less_k = False
        break

if all_less_k:
    print('0')
elif result > 0:
    print('1')
else:
    print('2')

assert mex([0, 1, 2]) == 3
assert mex([1, 2]) == 0
assert mex([0, 2]) == 1

assert g(0, 2) == 0
assert g(1, 2) == 0
assert g(2, 2) == 1
assert g(3, 2) == 1
