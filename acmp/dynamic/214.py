def solution(n, m):
    return 1 if ((n % 2) * 2) ^ ((m % 2) * 3) != 0 else 2


def read_integers():
    return [int(x) for x in input().split(' ')]


n, m = read_integers()
print(solution(n, m))

assert solution(2, 2) == 2
assert solution(1, 2) == 1
