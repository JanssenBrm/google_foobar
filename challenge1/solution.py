from collections import Counter

def solution(data, n):
    count = Counter(data)
    return [x for x in data if count[x] <= n]


if __name__ == '__main__':
    assert solution([1, 2, 3], 0) == []
    assert solution([1, 2, 2, 3, 3, 3, 4, 5, 5], 1) == [1,4]
    assert solution([1, 2, 3], 2) == [1,2,3]
