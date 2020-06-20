# memo = dict()


def solution(k, p):
    memo = [0, 0, 1, 1, 2]
    # memo[0] = 0
    # memo[1] = 0
    # memo[2] = 1
    # memo[3] = 1
    # memo[4] = 2
    if k < 5:
        return memo[k] % p
    last = memo[4]
    for i in range(5, k + 1):
        young = (0 if i % 2 == 1 else memo[i // 2])
        old = last
        last = (young + old) % p
        if i < k // 2 + 1:
            memo.append(last)
    return last % p


_in = [int(x) for x in input().split()]
print(solution(_in[0], _in[1]))

# print(solution(8, 10))
print(solution(360, 1000))
