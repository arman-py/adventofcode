data = """...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
..........."""


from collections import deque


if __name__ == "__main__":
    split_data = data.split("\n")
    lines_count = len(split_data)
    rows_count = len(split_data[0])
    final_steps = 26501365
    x, y = rows_count // 2, lines_count // 2
    v = {(x, y): 0}
    dist = 0
    q = deque()
    q.append((x, y))
    result = []
    steps = (x, x+lines_count, x+2*lines_count)
    while dist < max(steps):
        dist += 1
        q_2 = deque()
        while q:
            x, y = q.popleft()
            for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                nx, ny = dx + x, dy + y
                tx, ty = nx % len(split_data[0]), ny % len(split_data)
                if split_data[ty][tx] != '#' and (nx, ny) not in v:
                    v[(nx, ny)] = dist
                    q_2.append((nx, ny))
        q = q_2
        if dist in steps:
            result.append(len([x for x in v.values() if x % 2 == dist % 2]))
    f0, f1, f2 = result
    c = f0
    a = (f2 - 2 * f1 + f0) // 2
    b = f1 - f0 - a
    N = (final_steps - x) // lines_count
    print(a * N ** 2 + b * N + c)