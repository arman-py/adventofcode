data = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""


if __name__ == "__main__":
    split_data = data.split("\n")
    seeds = split_data[0][6:].split()
    maps = {int(x): int(x) for x in seeds}
    for line in split_data[1:]:
        if "map" in line:
            map_id = line
            maps = {y: y for x, y in maps.items()}
            continue
        if not line:
            continue
        mapping = [int(i) for i in line.split()]
        for pointer in maps:
            if mapping[1] <= pointer < mapping[1]+mapping[2]:
                maps[pointer] = mapping[0] + pointer - mapping[1]
    print(min(maps.values()))
