data = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""

# EMPTY_ROW_MULTIPLIER = 1
EMPTY_ROW_MULTIPLIER = 999999

if __name__ == "__main__":
    matrix = []
    empty_lines = set()
    empty_rows = set()
    split_data = data.split("\n")
    for index, line in enumerate(split_data):
        matrix.append([x for x in line])
        if "#" not in line:
            empty_lines.add(index)
    for i in range(len(split_data[0])):
        row = [x[i] for x in matrix]
        if "#" not in row:
            empty_rows.add(i)
    x = 0
    coordinates = []
    while x < len(matrix):
        y = 0
        while y < len(matrix[0]):
                if matrix[x][y] == "#":
                    coordinates.append([x, y])
                y += 1
        x += 1
    result = 0
    for i in range(len(coordinates)-1):
        for target in coordinates[i+1:]:
            source = coordinates[i]
            x_path = set(list(range(min(source[0], target[0]), max(source[0], target[0]))))
            y_path = set(list(range(min(source[1], target[1]), max(source[1], target[1]))))
            linear_m = empty_lines.intersection(x_path)
            rowar_m = empty_rows.intersection(y_path)

            dx = abs(source[0] - target[0]) + (len(rowar_m)*EMPTY_ROW_MULTIPLIER)
            dy = abs(source[1] - target[1]) + (len(linear_m)*EMPTY_ROW_MULTIPLIER)

            distance = abs(dx + dy)
            result += distance
    print(result)