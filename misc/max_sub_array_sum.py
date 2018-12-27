import math


def max_sub_array_sum_1(nums):
    """
    solution in O(n) using kadane's algorithm
    """
    if len(nums) == 0:
        return 0
    max_so_far = nums[0]
    max_current = nums[0]

    for i in range(1, len(nums)):
        max_current = max(max_current + nums[i], nums[i])
        max_so_far = max(max_so_far, max_current)

    return max_so_far


def max_crossing_subarray(x, l, m, r):
    left_sum = -math.inf
    s = 0
    for i in range(m, l - 1, -1):
        s += x[i]
        if s > left_sum:
            left_sum = s
    s = 0
    right_sum = -math.inf
    for i in range(m + 1, r + 1):
        s = s + x[i]
        if s > right_sum:
            right_sum = s

    return left_sum + right_sum


def max_sub_array_sum_2(nums, l, r):
    """
    solution in O(nlogn) using divide and conquer approach
    """
    if l == r:
        return nums[l]
    m = (l + r) // 2
    ans = max(max_sub_array_sum_2(nums, l, m), max_sub_array_sum_2(nums, m + 1, r),
              max_crossing_subarray(nums, l, m, r))
    return ans


print(max_sub_array_sum_1([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(max_sub_array_sum_2([-2, 1, -3, 4, -1, 2, 1, -5, 4], 0, 8))
