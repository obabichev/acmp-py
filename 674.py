def lines():
    with open('INPUT.TXT', "r") as f:
        return f.readlines()


memo = dict()


def solution(n):
    if n in memo:
        return memo[n]
    if n == 3:
        return 1
    if n < 3:
        return 0
    result = solution(n // 2) + solution(n // 2 + n % 2)
    memo[n] = result
    return result


# n = int(lines()[0])
# print (solution(n))

assert solution(3) == 1
assert solution(6) == 2
