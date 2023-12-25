data = """#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#"""

import sys
sys.setrecursionlimit(15000)


offsets_map = {
    "<": [(0, -1)],
    ">": [(0, 1)],
    "^": [(-1, 0)],
    "v": [(1, 0)],
}


def find_longest_path(y, x, end_y, end_x, visited, length):
    if (y, x) == (end_y, end_x):
        return length
    if (y, x) in visited:
        return 0
    current_visited = visited[:]
    current_visited.append((y, x))
    current_symbol = split_data[y][x]

    if current_symbol in offsets_map:
        offsets = offsets_map[current_symbol]
    else:
        offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    next_visits = []
    for offset in offsets:
        new_y, new_x = y + offset[0], x + offset[1]
        if new_y < 0 or new_x < 0 \
                or new_y >= lines_count or new_x >= rows_count \
                or split_data[new_y][new_x] == "#" \
                or (new_y, new_x) in current_visited:
            continue
        next_visits.append((new_y, new_x))

    if not next_visits:
        return 0

    next_paths = [
        find_longest_path(new_y, new_x, end_y, end_x, current_visited, length + 1) for (new_y, new_x) in next_visits
    ]

    return max(next_paths)


if __name__ == "__main__":
    split_data = data.split("\n")
    lines_count = len(split_data)
    rows_count = len(split_data[0])

    result = find_longest_path(0, split_data[0].index("."), lines_count - 1, split_data[-1].index("."), [], 0)
    print(result)
