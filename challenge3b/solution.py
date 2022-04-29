import random


def solution(s):
    c = 0
    n = int(s)
    while n > 1:
        if n % 2 == 0:
            n /= 2
        elif n % 4 == 1 or n == 3:
            n -= 1
        else:
            n += 1
        c += 1
    return c

assert solution('4') == 2
assert solution('15') == 5
print(solution(str(random.randint(10**306, 10**307 - 1))))
