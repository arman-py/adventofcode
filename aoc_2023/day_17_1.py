data = """2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533"""


import heapq


if __name__ == "__main__":
    split_data = data.split("\n")
    lines_count = len(split_data)
    rows_count = len(split_data[0])
    matrix = []
    for line in split_data:
        matrix.append([int(x) for x in line])
    q = [[0, 0, 0, -1, -1]]
    heapq.heapify(q)
    min_costs = {}
    full_path = []
    while len(q):
        dist, x, y, current_dir, dir_count = heapq.heappop(q)
        if (x, y, current_dir, dir_count) in min_costs:
            continue
        min_costs[(x, y, current_dir, dir_count)] = dist
        if x == lines_count - 1 and y == rows_count - 1:
            full_path.append(dist)
        for direction_key, (i, j) in enumerate([[-1, 0], [0, 1], [1, 0], [0, -1]]):
            if (direction_key + 2) % 4 == current_dir:
                continue
            new_x = x + i
            new_y = y + j
            new_dir = direction_key
            new_dir_count = 1 if new_dir != current_dir else dir_count + 1

            if 0 <= new_x < lines_count and 0 <= new_y < rows_count and new_dir_count <= 3:
                cost = matrix[new_x][new_y]
                heapq.heappush(q, [dist + cost, new_x, new_y, new_dir, new_dir_count])

    print(min(full_path))
