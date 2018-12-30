def int_sqrt_1(x):
    """
    solution in O(√n)
    """
    if x == 1 or x == 0:
        return x
    ans = 1
    while ans * ans <= x:
        ans += 1
    return ans - 1


def int_sqrt_2(x):
    """
    solution in O(log n) using binary search
    """
    if x == 1 or x == 0:
        return x
    s, e, ans = 1, x // 2, 0
    while s <= e:
        m = (s + e) // 2
        if m * m == x:
            return m
        if m * m < x:
            s = m + 1
            ans = m
        else:
            e = m - 1
    return ans


print(int_sqrt_1(168))
print(int_sqrt_2(168))
