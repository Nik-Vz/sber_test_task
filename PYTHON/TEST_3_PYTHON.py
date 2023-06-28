def get_biggest(nums):
    if len(nums) == 0:
        return -1

    txt = [str(num) for num in nums]
    txt.sort(reverse=True)

    i = 0
    while i != len(txt) - 1:
        if i < 0:
            i = 0

        a, b = txt[i], txt[i + 1]
        if (a, b) == max_num(a, b):
            i += 1
        else:
            txt[i], txt[i + 1] = max_num(a, b)
            i -= 1
    return int("".join(txt))


def max_num(a, b):
    if a + b >= b + a:
        return a, b

    else:
        return b, a
