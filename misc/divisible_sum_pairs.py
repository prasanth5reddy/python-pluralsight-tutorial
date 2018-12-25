# solution with O(n^2)
def divisible_sum_pairs_1(n, k, ar):
    ans = 0
    for j in range(n):
        for i in range(j):
            if (ar[i] + ar[j]) % k == 0:
                ans += 1

    return ans


# solution with O(n)
def divisible_sum_pairs_2(n, k, ar):
    mod_count = [0] * k
    for i in ar:
        mod_count[i % k] += 1

    ans = 0
    for i in range(int(k / 2) + 1):
        if i == 0:
            ans += int(mod_count[0] * (mod_count[0] - 1) / 2)
        elif i == k - i:
            ans += int(mod_count[int(k / 2)] * (mod_count[int(k / 2)] - 1) / 2)
        else:
            ans += int(mod_count[i] * (mod_count[k - i]))

    return ans


n, k, ar = 7, 3, [1, 3, 2, 6, 4, 5, 9]

print(divisible_sum_pairs_1(n, k, ar))
print(divisible_sum_pairs_2(n, k, ar))
