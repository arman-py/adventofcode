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


from collections import deque


def longest_path(graph, current, destination, distance=0):
    if current == destination:
        return distance
    best = 0
    path_seen.add(current)
    for neighbor, weight in graph[current]:
        if neighbor in path_seen:
            continue
        new_length = longest_path(graph, neighbor, destination, distance + weight)
        if new_length > best:
            best = new_length
    path_seen.remove(current)
    return best


if __name__ == "__main__":
    split_data = data.split("\n")
    matrix = []
    for line in split_data:
        matrix.append([x for x in line])
    height, width = len(matrix), len(matrix[0])
    matrix[0][1] = '#'
    matrix[height - 1][width - 2] = '#'
    path_seen = set()
    source = (1, 1)
    destination = (height - 2, width - 2)
    graph = {}
    q = deque([source])
    seen = set()
    while q:
        xy = q.popleft()
        if xy in seen:
            continue
        seen.add(xy)
        q_2 = deque([(xy, 0)])
        seen_2 = set()
        adjacent_nodes = []
        while q_2:
            xy_2, dist = q_2.popleft()
            seen_2.add(xy_2)
            x, y = xy_2
            neighbors = [(i, j) for i, j in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)] if matrix[i][j] != "#"]
            for n in neighbors:
                if n in seen_2:
                    continue
                k, o = n
                if n == destination or n == source or \
                        len([(i, j) for i, j in [(k + 1, o), (k - 1, o), (k, o + 1), (k, o - 1)] if
                             matrix[i][j] != "#"]) > 2:
                    adjacent_nodes.append((n, dist + 1))
                    continue
                q_2.append((n, dist + 1))
        for n, weight in adjacent_nodes:
            if xy in graph:
                graph[xy].append((n, weight))
            else:
                graph[xy] = [(n, weight)]
            q.append(n)
    print(longest_path(graph, (1, 1), (height - 2, width - 2)) + 2)
