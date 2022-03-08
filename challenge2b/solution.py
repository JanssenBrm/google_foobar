import numpy as np

def f(n, b):
    n_sorted = "".join(sorted(n))
    n_int = int(n_sorted, b)
    n_rev_int = int(n_sorted[::-1],b)
    diff = np.base_repr(n_rev_int - n_int, base = b)
    return diff.zfill(len(n))


def solution(n, b):
    power = lam = 1
    x = n
    y = f(n, b)
    while x != y:
        if power == lam:
            x = y
            power *= 2
            lam = 0
        y = f(y,b)
        lam += 1
    return lam


assert solution('1211', 10) == 1
assert solution('210022', 3) == 3
