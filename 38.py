memo = dict()


def win(numbers, i, j):
    '''
    How much players win if he starts with subarray with elements from i to j
    return (x, y) x - win of current player, y - win of other player
    '''
    if i == j:
        return numbers[i], 0

    if (i, j) in memo:
        return memo[(i, j)]

    left = win(numbers, i + 1, j)
    first = (numbers[i] + left[1], left[0])
    right = win(numbers, i, j - 1)
    second = (numbers[j] + right[1], right[0])
    result = first if first[0] > second[0] else second
    memo[(i, j)] = result
    return result


def solution(numbers):
    win1, win2 = win(numbers, 0, len(numbers) - 1)
    if win1 > win2:
        return 1
    elif win2 > win1:
        return 2
    else:
        return 0

n = int(input())
numbers = [int(x) for x in input().split()]
print(solution(numbers))

# assert solution([3, 2, 5, 4]) == 1
# assert solution([2, 1, 3, 2, 9, 1, 2, 3, 1]) == 2
