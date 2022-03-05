def solution(x, y):
    return str(int(1 + ((y - 1) * y) / 2) + sum(range(y + 1, y + x)))


if __name__ == '__main__':

    print('-----------------------------------')
    print('PYRAMID CHECK')
    print('-----------------------------------')

    size = 6
    rows = list()
    for row in range(1, size):
        rowText = '| '
        for col in range(1, size + 1 - row):
            rowText += solution(col, row) + ' '
        rows.append(rowText)

    rows.reverse()
    print('\n'.join(rows))

    print('-----------------------------------')
    print('TEST CASES')
    print('-----------------------------------')

    for x, y, expected in [
        (1, 1, 1),
        (2, 1, 3),
        (3, 1, 6),
        (4, 1, 10),
        (1, 2, 2),
        (2, 2, 5),
        (3, 2, 9),
        (1, 3, 4),
        (2, 3, 8),
        (1, 4, 7),
        (5, 10, 96)
    ]:
        result = solution(x, y)
        print(f'solution({x}, {y}) === {result} ({expected})')
        assert result == str(expected)
