def solution(n, stairs):
    solutions = [(stairs[0], -1)]  # (<sum>, <prev_step>)

    if stairs[0] > 0:
        solutions.append((stairs[0] + stairs[1], 0))
    else:
        solutions.append((stairs[1], -1))

    for i in range(2, len(stairs)):
        if solutions[i - 1][0] > solutions[i - 2][0]:
            solutions.append((solutions[i - 1][0] + stairs[i], i - 1))
        else:
            solutions.append((solutions[i - 2][0] + stairs[i], i - 2))

    result_sum = solutions[-1][0]
    current_step = solutions[-1][1]
    steps = [n - 1]
    while current_step != -1:
        steps.append(current_step)
        current_step = solutions[current_step][1]

    steps.reverse()

    return result_sum, steps


n = int(input())
stairs = [int(x) for x in input().split()]

sum, steps = solution(n, stairs)
print(sum)
print(' '.join(map(lambda x: str(x + 1), steps)))

