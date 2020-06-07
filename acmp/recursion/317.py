def solution(x, y, z, w):
    result = 0
    for i in range(0, w // x + 1):
        for j in range(0, (w - i * x) // y + 1):
            if (w - i * x - j * y) % z == 0:
                result += 1
    return result


_in = [int(x) for x in input().split()]
print(solution(_in[0], _in[1], _in[2], _in[3]))

# print(solution(10, 25, 15, 40))

assert solution(10, 25, 15, 40) == 3
