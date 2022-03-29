
def solution(l):
    divs = [0] * len(l)
    count = 0

    for i in range(0, len(l)):
        for j in range(0, i):
            if l[i] % l[j] == 0:
                divs[i] = divs[i] + 1
                count = count + divs[j]
    return count


assert solution([1, 2, 3, 4, 5, 6]) == 3
assert solution([1, 1, 1]) == 1
