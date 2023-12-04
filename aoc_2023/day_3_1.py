data = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""


if __name__ == "__main__":
    clarified_data = data.replace("\n", "")
    line_length = len(data.split()[0])
    index = 0
    result = 0
    while index < len(clarified_data):
        if not clarified_data[index].isdigit():
            index += 1
            continue
        initial_index = index
        while clarified_data[index].isdigit():
            index += 1
        adjacent_symbols = ""

        if initial_index-line_length-1 >= 0:
            adjacent_symbols += clarified_data[initial_index-line_length-1:index-line_length+1]
        if initial_index-1 >= 0:
            adjacent_symbols += clarified_data[initial_index-1]
        adjacent_symbols += clarified_data[index]
        adjacent_symbols += clarified_data[initial_index+line_length-1:index+line_length+1]

        if adjacent_symbols != "."*len(adjacent_symbols):
            result += int(clarified_data[initial_index:index])
    print(result)