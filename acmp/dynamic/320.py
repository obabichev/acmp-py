memo = dict()


def rec(b, p):
    if b == 0 or p == 0:
        return 1
    if (b, p) not in memo:
        memo[(b, p)] = rec(b - 1, p) + rec(b, p - 1)
    return memo[(b, p)]


def solution(m, n):
    result = 0
    for i in range(n // m + 1):
        current = rec(i, n - i * m)
        # print('current', (i, n - i * m, current))
        result += current
    return result


first = input().split()
m = int(first[0])
n = int(first[1])
print(solution(m, n))

# print('solution(2, 5)', solution(2, 5))

assert solution(4, 6) == 4
assert solution(8, 11) == 5
assert solution(9, 12) == 5
