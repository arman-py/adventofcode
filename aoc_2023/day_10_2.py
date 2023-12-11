data = """FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L"""

coordinates = {
    (-1, 0): ["F", "7", "|", "S"],
    (1, 0): ["J", "L", "|", "S"],
    (0, -1): ["-", "F", "L", "S"],
    (0, 1): ["-", "7", "J", "S"],
}

symbols_map = {
    "|": {(-1, 0): coordinates[(-1, 0)], (1, 0): coordinates[(1, 0)]},
    "L": {(-1, 0): coordinates[(-1, 0)], (0, 1): coordinates[(0, 1)]},
    "J": {(-1, 0): coordinates[(-1, 0)], (0, -1): coordinates[(0, -1)]},
    "-": {(0, -1): coordinates[(0, -1)], (0, 1): coordinates[(0, 1)]},
    "F": {(1, 0): coordinates[(1, 0)], (0, 1): coordinates[(0, 1)]},
    "7": {(1, 0): coordinates[(1, 0)], (0, -1): coordinates[(0, -1)]}
}


if __name__ == "__main__":
    matrix = []
    split_data = data.split("\n")
    clear_data = "".join(split_data)
    line_length = len(split_data[0])

    start_index = data.index("S")
    for line in split_data:
        matrix.append([x for x in line])
    x = start_index//line_length
    old_coordinates = [x, ((start_index-x) % line_length)]
    new_coordinates = []
    pipe_path = set()
    pipe_path.add((line_length*old_coordinates[0]) + old_coordinates[1])
    for changes, symbols in coordinates.items():
        if matrix[old_coordinates[0]+changes[0]][old_coordinates[1]+changes[1]] in symbols:
            new_coordinates = [old_coordinates[0]+changes[0], old_coordinates[1]+changes[1]]
            break
    index = 0
    while True:
        pipe_path.add((line_length*new_coordinates[0])+new_coordinates[1])
        if matrix[new_coordinates[0]][new_coordinates[1]] == "S":
            break

        for changes, symbols in symbols_map[matrix[new_coordinates[0]][new_coordinates[1]]].items():
            if new_coordinates[0]+changes[0] != old_coordinates[0] or new_coordinates[1]+changes[1] != old_coordinates[1]:
                next_coordinate = [new_coordinates[0]+changes[0], new_coordinates[1]+changes[1]]
        old_coordinates = new_coordinates
        new_coordinates = next_coordinate
    result = 0
    for x in range(len(clear_data)):
        if x in pipe_path:
            continue
        right_outside_flag = True
        left_outside_flag = True
        y = x
        while y > 0:
            if y in pipe_path and clear_data[y] in ["L", "F", "-"]:
                right_outside_flag = not right_outside_flag
            if y in pipe_path and clear_data[y] in ["7", "J", "-"]:
                left_outside_flag = not left_outside_flag
            y -= line_length

        if not right_outside_flag and not left_outside_flag:
            result += 1
    print(result)
