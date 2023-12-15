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
    result = 0
    for row_index in range(len(split_data[0])):
        row = [x[row_index] for x in split_data]
        empty_rounds = ("".join(row)).split("#")
        new_empty_rounds = "#".join([("O"*rr.count("O"))+("."*rr.count(".")) for rr in empty_rounds])
        result += sum([height-i if x == "O" else 0 for i, x in enumerate(new_empty_rounds)])

    print(result)
