data = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""


if __name__ == "__main__":
    matrix = []
    split_data = data.split('\n')
    height = len(split_data)
    for line in split_data:
        matrix.append([x for x in line])
    indo = 0
    cache = []
    special_line = None
    while True:
        if " ".join(["".join(y) for y in matrix]) in cache:
            start_index = cache.index(" ".join(["".join(y) for y in matrix]))
            finish_index = indo
            exact_one = (1000000000-start_index) % (finish_index - start_index)
            special_line = cache[start_index:][exact_one]
            break
        cache.append(" ".join(["".join(y) for y in matrix]))
        indo += 1
        for row_index in range(len(matrix[0])):
            row = [x[row_index] for x in matrix]
            empty_rounds = ("".join(row)).split("#")
            new_empty_rounds = "#".join([("O"*rr.count("O"))+("."*rr.count(".")) for rr in empty_rounds])
            for line_index in range(len(matrix)):
                matrix[line_index][row_index] = new_empty_rounds[line_index]
        for line_index in range(len(matrix)):
            empty_rounds = ("".join(matrix[line_index])).split("#")
            new_empty_rounds = "#".join([("O" * rr.count("O")) + ("." * rr.count(".")) for rr in empty_rounds])
            matrix[line_index] = [x for x in new_empty_rounds]
        for row_index in range(len(matrix[0])):
            row = [x[row_index] for x in matrix]
            empty_rounds = ("".join(row)).split("#")
            new_empty_rounds = "#".join([("."*rr.count(".")) + ("O"*rr.count("O")) for rr in empty_rounds])
            for line_index in range(len(matrix)):
                matrix[line_index][row_index] = new_empty_rounds[line_index]
        for line_index in range(len(matrix)):
            empty_rounds = ("".join(matrix[line_index])).split("#")
            new_empty_rounds = "#".join([("." * rr.count(".")) + ("O" * rr.count("O"))  for rr in empty_rounds])
            matrix[line_index] = [x for x in new_empty_rounds]

    result = 0
    for index, line in enumerate(special_line.split()):
        result += (height - index) * line.count("O")

    print(result)
