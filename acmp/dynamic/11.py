def solution(k, n):
    results = [1]
    for i in range(1, n + 1):
        current = 0
        for j in range(max(0, i - k), i):
            current += results[j]
        results.append(current)
    return results[n]


_in = [int(x) for x in input().split()]
print(solution(_in[0], _in[1]))
