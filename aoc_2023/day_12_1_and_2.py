data = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""


def decrease_first_value(c):
    return [c[0]-1] + c[1:]


def arrangement(cache, condition_line, counts, flag):
    key = (condition_line, tuple(counts), flag)
    if key in cache:
        return cache[key]
    if not counts:
        return 0 if "#" in condition_line else 1
    elif not condition_line:
        return 0 if sum(counts) else 1
    elif counts[0] == 0:
        arrangement_count = arrangement(cache, condition_line[1:], counts[1:], False) if condition_line[0] in ["?", "."] else 0
    elif flag:
        arrangement_count = arrangement(cache, condition_line[1:], decrease_first_value(counts), True) if condition_line[0] in ["?", "#"] else 0
    elif condition_line[0] == "#":
        arrangement_count = arrangement(cache, condition_line[1:], decrease_first_value(counts), True)
    elif condition_line[0] == ".":
        arrangement_count = arrangement(cache, condition_line[1:], counts, False)
    else:
        arrangement_count = arrangement(cache, condition_line[1:], counts, False) + arrangement(cache, condition_line[1:], decrease_first_value(counts), True)

    cache[key] = arrangement_count
    return arrangement_count


if __name__ == "__main__":
    split_data = data.split("\n")
    result = 0
    for line in split_data:
        line_parts = line.split()
        condition = line_parts[0]
        broken_sizes = [int(x) for x in line_parts[1].split(",")]
        # result += arrangement({}, condition, broken_sizes, False)
        result += arrangement({}, '?'.join([condition for x in range(5)]), broken_sizes * 5, False)

    print(result)
