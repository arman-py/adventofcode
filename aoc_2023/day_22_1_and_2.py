data = """1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9"""


def coordinates(brick):
    coord = []
    for x in range(brick[0], brick[3] + 1):
        for y in range(brick[1], brick[4] + 1):
            for z in range(brick[2], brick[5] + 1):
                coord.append((x, y, z))
    return coord


def add_falling_bricks(brick):
    if brick in falling_bricks:
        return
    falling_bricks.add(brick)
    if brick in above:
        for parent in above[brick]:
            if not len(set(below[parent]) - falling_bricks):
                add_falling_bricks(parent)


if __name__ == "__main__":
    split_data = data.split("\n")
    bricks = []
    for line in split_data:
        part_1, part_2 = line.split("~")
        brick = part_1.split(",")
        brick.extend(part_2.split(","))
        bricks.append(brick)
    numerated_bricks = [tuple([int(x) for x in xes] + [i]) for i, xes in enumerate(bricks)]
    numerated_bricks.sort(key=lambda brick: brick[2])
    occupied = {}
    fallen = []
    for brick in numerated_bricks:
        while True:
            next_position = (brick[0], brick[1], brick[2] - 1, brick[3], brick[4], brick[5] - 1, brick[6])
            if not any(pos in occupied for pos in coordinates(next_position)) and next_position[2] > 0:
                brick = next_position
            else:
                for pos in coordinates(brick):
                    occupied[pos] = brick
                fallen.append(brick)
                break

    above = {}
    below = {}
    for brick in fallen:
        brick_coordinates = coordinates(brick)
        brick_under = (brick[0], brick[1], brick[2] - 1, brick[3], brick[4], brick[5] - 1, brick[6])
        for pos in coordinates(brick_under):
            if pos in occupied and pos not in brick_coordinates:
                if occupied[pos] in above:
                    above[occupied[pos]].append(brick)
                else:
                    above[occupied[pos]] = [brick]
                if brick in below:
                    below[brick].append(occupied[pos])
                else:
                    below[brick] = [occupied[pos]]

    part_1_result = 0
    part_2_result = 0
    for brick in fallen:
        falling_bricks = set()
        add_falling_bricks(brick)
        would_fall = len(falling_bricks)
        if would_fall == 1:
            part_1_result += 1
        else:
            part_2_result += would_fall - 1
    print(part_1_result)
    print(part_2_result)
