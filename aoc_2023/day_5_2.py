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
    seeds_coordinates = [int(x) for x in split_data[0][6:].split()]
    map_id = "seeds:"
    old_list = []
    new_list = []
    maps = {
        "seed-to-soil map:": [],
        "soil-to-fertilizer map:": [],
        "fertilizer-to-water map:": [],
        "water-to-light map:": [],
        "light-to-temperature map:": [],
        "temperature-to-humidity map:": [],
        "humidity-to-location map:": [],
    }
    index = 0
    while index < len(seeds_coordinates):
        new_list.append([seeds_coordinates[index],
                         seeds_coordinates[index] + seeds_coordinates[index + 1] - 1])
        index += 2
    for line in split_data[1:]:
        if "map" in line:
            map_id = line
            continue
        if not line:
            continue
        ranges = [int(i) for i in line.split()]
        source_range = [ranges[1], ranges[1] + ranges[2] - 1]
        destination_range = [ranges[0], ranges[0] + ranges[2] - 1]
        maps[map_id].append({"source_range": source_range, "destination_range": destination_range})

    for level_name, mapping in maps.items():
        old_list = new_list[:]
        new_list = []
        while old_list:
            seed = old_list.pop()
            for mapping_elem in mapping:
                source_range = mapping_elem['source_range']
                destination_range = mapping_elem['destination_range']
                if seed[0] > source_range[1] or seed[1] < source_range[0]:
                    continue
                elif seed[0] < source_range[0] and seed[1] > source_range[1]:
                    new_list.append([destination_range[0], destination_range[1]])
                    old_list.append([seed[0], source_range[0]-1])
                    old_list.append([source_range[1]+1, seed[1]])
                    break
                elif seed[0] >= source_range[0] and seed[1] <= source_range[1]:
                    new_list.append([seed[0] + destination_range[0] - source_range[0],
                                     seed[1] + destination_range[1] - source_range[1]])
                    break
                elif seed[0] < source_range[0] and seed[1] <= source_range[1]:
                    new_list.append([destination_range[0], seed[1] + destination_range[1] - source_range[1]])
                    old_list.append([seed[0], source_range[0]-1])
                    break
                elif seed[0] >= source_range[0] and seed[1] > source_range[1]:
                    new_list.append([seed[0] + destination_range[0] - source_range[0], destination_range[1]])
                    old_list.append([source_range[1]+1, seed[1]])
                    break
            else:
                new_list.append(seed)
    print(min(*[x[0] for x in new_list]))

