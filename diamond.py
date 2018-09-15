def diamond(height):
    """Return a string resembling a diamond of specified height (measured in lines).
    height must be an even integer.
    """
    ans = ''
    half_height = height // 2
    a, b = '/', '\\'
    for i in range(1, height + 1):
        if i - 1 == half_height:
            a, b = b, a
        if i <= half_height:
            nchars = i
        else:
            nchars = height - i + 1
        ans += (a * nchars).rjust(half_height)
        ans += (b * nchars).ljust(half_height)
        ans += '\n'

    return ans


print(diamond(8))
