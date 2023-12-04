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
    asterix = {x: [] for x, d in enumerate(clarified_data)}
    while index < len(clarified_data):
        if not clarified_data[index].isdigit():
            index += 1
            continue
        initial_index = index
        while clarified_data[index].isdigit():
            index += 1
        adjacent_symbols = ""

        if initial_index-line_length-1 >= 0:
            if "*" in clarified_data[initial_index-line_length-1:index-line_length+1]:
                asterix[clarified_data.index("*", initial_index-line_length-1, index-line_length+1)].append(int(clarified_data[initial_index:index]))
        if initial_index-1 >= 0:
            if "*" == clarified_data[initial_index-1]:
                asterix[initial_index-1].append(int(clarified_data[initial_index:index]))
        if "*" == clarified_data[index]:
            asterix[index].append(int(clarified_data[initial_index:index]))
        if "*" in clarified_data[initial_index+line_length-1:index+line_length+1]:
            asterix[clarified_data.index("*", initial_index+line_length-1, index+line_length+1)].append(int(
                clarified_data[initial_index:index]))

    for x in asterix.values():
        if len(x) == 2:
            result += x[0]*x[1]
    print(result)