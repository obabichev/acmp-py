def bin_search(arr, num):
    left = 0
    right = len(arr) - 1
    while right - left > 1:
        mid = left + (right - left) // 2
        if arr[mid] == num:
            return mid
        if arr[mid] < num:
            left = mid
        else:
            right = mid

    if arr[left] >= num:
        return left
    else:
        return right


def solution(nums):
    d = [100000 for x in nums]
    d[0] = nums[0]

    result = 1

    for i in range(1, len(nums)):
        num = nums[i]
        index = bin_search(d, num)
        if d[index] > num:
            d[index] = num
            result = max(result, index + 1)

    return result


n = int(input())
nums = [int(x) for x in input().split()]
print(solution(nums))

assert solution([3, 29, 5, 5, 28, 6]) == 3

assert bin_search([1, 3, 5, 7, 9, 11, 13, 15], 6) == 3
assert bin_search([1, 3, 5, 7, 9, 11, 13, 15], 5) == 2
assert bin_search([1, 3, 5, 7, 9, 11, 13, 15], 7) == 3
assert bin_search([1, 3, 5, 7, 9, 11, 13, 15], 1) == 0
assert bin_search([1, 3, 5, 7, 9, 11, 13, 15], 15) == 7
assert bin_search([1, 3, 5, 7], 100) == 3
assert bin_search([1, 3, 5, 7], 4) == 2
