import math


game_logs = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""


max_count = {
    "red": 12,
    "blue": 14,
    "green": 13
}


if __name__ == "__main__":
    powers_sum = 0
    for line in game_logs.split("\n"):
        max_count_for_current_set = {
            "red": 0,
            "blue": 0,
            "green": 0
        }
        game_id = int(line[5:].split(":")[0])
        game_sequence = line[5:].split(":")[1][1:]
        for game_set in game_sequence.split(";"):
            set_data = game_set.split()
            index = 0
            while index < len(set_data):
                color_name = set_data[index + 1].replace(",", "")
                if max_count_for_current_set[color_name] < int(set_data[index]):
                    max_count_for_current_set[color_name] = int(set_data[index])

                index += 2

        powers_sum += math.prod(max_count_for_current_set.values())
    print(powers_sum)