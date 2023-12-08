data = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""

mapping = {}


if __name__ == "__main__":
    split_data = data.split("\n")
    instructions = split_data[0]
    for element in split_data[2:]:
        mapping[element[:3]] = {"L": element[7:10], "R": element[12:15]}
    index = 0
    coordinate = "AAA"
    while True:
        if coordinate == "ZZZ":
            break
        else:
            coordinate = mapping[coordinate][instructions[index % len(instructions)]]
        index += 1
    print(index)
