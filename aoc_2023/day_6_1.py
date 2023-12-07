data = """Time:        35     69     68     87
Distance:   213   1168   1086   1248"""


import math


if __name__ == "__main__":
    time_str = data.split("\n")[0].split(':')[1]
    distance_str = data.split("\n")[1].split(':')[1]
    times = [int(x) for x in time_str.split()]
    distances = [int(x) for x in distance_str.split()]
    wins = [0 for x in range(len(times))]
    index = 0
    while index < len(times):
        time = times[index]
        distance = distances[index]
        for x in range(1, time):
            if x*(time-x) > distance:
                wins[index] += 1
        index += 1
    print(math.prod(wins))
    