data = """Time:      7  15   30
Distance:  9  40  200"""


if __name__ == "__main__":
    time_str = data.split("\n")[0].split(':')[1]
    distance_str = data.split("\n")[1].split(':')[1]
    time = int("".join([x for x in time_str.split()]))
    distance = int("".join([x for x in distance_str.split()]))
    min_limit = 0
    max_limit = 0
    index = 0
    # TODO can be optimized to binary search
    for x in range(1, time):
        if x*(time-x) > distance:
            min_limit = x
            break
    for x in range(time-2, 0, -1):
        if x*(time-x) > distance:
            max_limit = x
            break

    print(max_limit-min_limit+1)
