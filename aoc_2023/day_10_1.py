data="""-L|F7
7S-7|
L|7||
-L-J|
L|-JF"""

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
    line_length = len(split_data[0])
    start_index = data.index("S")
    for line in split_data:
        matrix.append([x for x in line])
    pipe_length = 0
    x = start_index//line_length
    old_coordinates = [x, ((start_index-x) % line_length)]
    new_coordinates = []
    for changes, symbols in coordinates.items():
        if matrix[old_coordinates[0]+changes[0]][old_coordinates[1]+changes[1]] in symbols:
            new_coordinates = [old_coordinates[0]+changes[0], old_coordinates[1]+changes[1]]
            break
    index = 0
    while True:
        pipe_length += 1
        if matrix[new_coordinates[0]][new_coordinates[1]] == "S":
            break

        for changes, symbols in symbols_map[matrix[new_coordinates[0]][new_coordinates[1]]].items():
            if new_coordinates[0]+changes[0] != old_coordinates[0] or new_coordinates[1]+changes[1] != old_coordinates[1]:
                next_coordinate = [new_coordinates[0]+changes[0], new_coordinates[1]+changes[1]]
        old_coordinates = new_coordinates
        new_coordinates = next_coordinate

    print(pipe_length//2)
