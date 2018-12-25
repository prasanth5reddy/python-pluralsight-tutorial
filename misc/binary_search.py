def binary_search(arr, t):
    """
    returns index of the target. If not found return -1
    time complexity O(log n)
    """
    l = 0
    r = len(arr) - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] == t:
            return m
        elif nums[m] < t:
            l = m + 1
        else:
            r = m - 1
    return -1


nums = [1, 3, 5, 8, 11, 13, 25, 34]
target = 11
print(binary_search(nums, target))
