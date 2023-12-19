data = """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)"""


directions_map = {
    "0": [0, 1],
    "2": [0, -1],
    "3": [-1, 0],
    "1": [1, 0],
}

if __name__ == "__main__":
    split_data = data.split("\n")
    steps_sum = 0
    area = 0
    x = 0
    y = 0
    for line in split_data:
        line_split = line.split()
        hexa_string = line_split[2]
        direction = hexa_string[-2]
        steps = int(hexa_string[2:-2], 16)
        direction_coordinates = directions_map[direction]
        steps_sum += steps
        diff_x, diff_y = direction_coordinates
        diff_x, diff_y = diff_x * steps, diff_y * steps
        x, y = x + diff_x, y + diff_y
        area += x * diff_y

    print(abs(area) + steps_sum // 2 + 1)
