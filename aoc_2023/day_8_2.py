data = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""


from math import lcm


if __name__ == "__main__":
    split_data = data.split("\n")
    instructions = split_data[0]
    list_of_a = {}
    mapping = {}
    for element in split_data[2:]:
        if element[:3][-1] == "A":
            list_of_a[element[:3]] = 0
        mapping[element[:3]] = {"L": element[7:10], "R": element[12:15]}
    for item in list_of_a.keys():
        index = 0
        coordinate = item
        while True:
            if coordinate[-1] == "Z":
                break
            else:
                coordinate = mapping[coordinate][instructions[index % len(instructions)]]
            index += 1
        list_of_a[item[:3]] = index

    print(lcm(*list_of_a.values()))
