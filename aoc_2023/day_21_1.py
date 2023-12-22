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
    q = deque()
    q.append((rows_count // 2, lines_count // 2, 0))
    o_64 = set()
    visited = set()
    while q:
        x, y, steps = q.popleft()
        if (x, y, steps) in visited:
            continue
        visited.add((x, y, steps))
        if steps == 64:
            o_64.add((x, y))
        else:
            if x > 0:
                if split_data[y][x - 1] != "#":
                    q.append((x - 1, y, steps + 1))
            if x < rows_count - 1:
                if split_data[y][x + 1] != "#":
                    q.append((x + 1, y, steps + 1))
            if y > 0:
                if split_data[y - 1][x] != "#":
                    q.append((x, y - 1, steps + 1))
            if y < lines_count - 1:
                if split_data[y + 1][x] != "#":
                    q.append((x, y + 1, steps + 1))
    print(len(o_64))
