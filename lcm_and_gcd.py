def gcd_of_two(a, b):
    if b == 0:
        return a
    else:
        return gcd_of_two(b, a % b)


def lcm_of_two(a, b):
    return a * b // gcd_of_two(a, b)


print(gcd_of_two(12, 16))
print(lcm_of_two(48, 36))


def gcd_of_list(l):
    if len(l) == 0:
        return
    gcd = l[0]
    for i in l[1:]:
        gcd = gcd_of_two(i, gcd)
    return gcd


def lcm_of_list(l):
    if len(l) == 0:
        return
    lcm = l[0]
    for i in l[1:]:
        lcm = i * lcm // gcd_of_two(i, lcm)
    return lcm


print(gcd_of_list([12, 48, 18]))
print(lcm_of_list([48, 36, 96]))
