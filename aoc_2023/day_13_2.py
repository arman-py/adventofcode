data = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""


if __name__ == "__main__":
    split_data = data.split("\n")
    split_data.append('')
    matrix = []
    lines = 0
    rows = 0
    for line in split_data:
        if line:
            matrix.append([element for element in line])
        else:
            for i in range(1, len(matrix)):
                length = min(i, len(matrix)-i)
                difference = [(k, o) for k, row in enumerate(matrix[i-length:i]) for o, x in enumerate(row) if matrix[i:i+length][::-1][k][o] != x]

                if len(difference) == 1:
                    rows += i
                    break
            tmatrix = list(map(list, zip(*matrix)))
            for i in range(1, len(tmatrix)):
                length = min(i, len(tmatrix) - i)
                difference = [(k, o) for k, row in enumerate(tmatrix[i - length:i]) for o, x in enumerate(row) if
                              tmatrix[i:i + length][::-1][k][o] != x]
                if len(difference) == 1:
                    lines += i
                    break
            matrix = []
    result = lines + (rows * 100)
    print(result)
