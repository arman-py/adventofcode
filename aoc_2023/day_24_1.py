data = """19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3"""


if __name__ == "__main__":
    result = 0
    combination = []
    split_data = data.split("\n")

    for line in split_data:
        line_parts = line.split("@")
        position = [int(x) for x in line_parts[0].replace(" ", "").split(",")]
        velocity = [int(x) for x in line_parts[1].replace(" ", "").split(",")]
        combination.append([position, velocity])
    for i in range(len(combination)):
        for j in range(i, len(combination)):
            hail_1, velocity_1 = combination[i]
            hail_2, velocity_2 = combination[j]
            if velocity_2[0] * velocity_1[1] - velocity_2[1] * velocity_1[0] == 0:
                continue
            u = ((hail_2[1] - hail_1[1]) * velocity_2[0] - (hail_2[0] - hail_1[0]) * velocity_2[1]) / (velocity_2[0] * velocity_1[1] - velocity_2[1] * velocity_1[0])
            v = ((hail_2[1] - hail_1[1]) * velocity_1[0] - (hail_2[0] - hail_1[0]) * velocity_1[1]) / (velocity_2[0] * velocity_1[1] - velocity_2[1] * velocity_1[0])

            if u < 0 or v < 0:
                continue

            xi = hail_2[0] + velocity_2[0] * v
            yi = hail_2[1] + velocity_2[1] * v
            if 200000000000000 <= xi <= 400000000000000 and 200000000000000 <= yi <= 400000000000000:
                result += 1
    print(result)
