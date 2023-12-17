data = r""".|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....""".replace("\\", "o")


def calculate_tiles(lights, directions, matrix):
    hash_lights = set()
    hash_point_direction = {}
    directions_for_empty_map = {
        "R": [0, 1],
        "L": [0, -1],
        "U": [-1, 0],
        "D": [1, 0],
    }
    while lights:
        x, y = lights[0]
        try:
            matrix[x][y]
        except Exception:
            del lights[0]
            del directions[0]
            continue
        if lights[0] in hash_point_direction:
            if directions[0] in hash_point_direction[lights[0]]:
                del lights[0]
                del directions[0]
                continue
            else:
                hash_point_direction[lights[0]].append(directions[0])
        else:
            hash_point_direction[lights[0]] = [directions[0]]
        hash_lights.add(lights[0])
        if matrix[x][y] == ".":
            new_directions = directions_for_empty_map[directions[0]]
            if x + new_directions[0] >= 0 and y + new_directions[1] >= 0:
                lights.append((x + new_directions[0], y + new_directions[1]))
                directions.append(directions[0])
        elif matrix[x][y] == "/":
            if directions[0] == "R":
                if x - 1 >= 0:
                    lights.append((x - 1, y))
                    directions.append("U")
            elif directions[0] == "L":
                lights.append((x + 1, y))
                directions.append("D")
            elif directions[0] == "U":
                lights.append((x, y + 1))
                directions.append("R")
            elif directions[0] == "D":
                if y - 1 >= 0:
                    lights.append((x, y - 1))
                    directions.append("L")
        elif matrix[x][y] == "o":  # "\"
            if directions[0] == "R":
                lights.append((x + 1, y))
                directions.append("D")
            elif directions[0] == "L":
                if x - 1 >= 0:
                    lights.append((x - 1, y))
                    directions.append("U")
            elif directions[0] == "U":
                if y - 1 >= 0:
                    lights.append((x, y - 1))
                    directions.append("L")
            elif directions[0] == "D":
                lights.append((x, y + 1))
                directions.append("R")
        elif matrix[x][y] == "-":
            if directions[0] in ["D", "U"]:
                if y - 1 >= 0:
                    lights.append((x, y - 1))
                    directions.append("L")
                lights.append((x, y + 1))
                directions.append("R")
            else:
                new_directions = directions_for_empty_map[directions[0]]
                lights.append((x + new_directions[0], y + new_directions[1]))
                directions.append(directions[0])
        elif matrix[x][y] == "|":
            if directions[0] in ["L", "R"]:
                if x - 1 >= 0:
                    lights.append((x - 1, y))
                    directions.append("U")
                lights.append((x + 1, y))
                directions.append("D")
            else:
                new_directions = directions_for_empty_map[directions[0]]
                if x + new_directions[0] >= 0 and y + new_directions[1] >= 0:
                    lights.append((x + new_directions[0], y + new_directions[1]))
                    directions.append(directions[0])
        del lights[0]
        del directions[0]
    return len(hash_lights)


if __name__ == "__main__":
    matrix = []
    split_data = data.split("\n")
    for line in split_data:
        matrix.append([x for x in line])
    results = []
    for xi in range(len(matrix)):
        results.append(calculate_tiles(
            [(0, xi)],
            ["D"],
            matrix
        ))
        results.append(calculate_tiles(
            [(len(matrix[0])-1, xi)],
            ["U"],
            matrix
        ))
    for yi in range(len(matrix[0])):
        results.append(calculate_tiles(
            [(yi, 0)],
            ["R"],
            matrix
        ))
        results.append(calculate_tiles(
            [(yi, len(matrix)-1)],
            ["L"],
            matrix
        ))
    print(max(results))