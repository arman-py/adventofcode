data = """broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a"""


if __name__ == "__main__":
    split_data = data.split("\n")
    input_configuration = {}
    for line in split_data:
        name, target = line.split(" -> ")
        target = target.split(", ")
        is_flip_flop = name[0] == "%"
        is_conjunction = name[0] == "&"
        if is_flip_flop:
            state = False
            name = name[1:]
        elif is_conjunction:
            state = {}
            name = name[1:]
        else:
            state = None
        input_configuration[name] = [target, is_flip_flop, is_conjunction, state]

    for conjunction_name, conjunction_state in {
        x: input_configuration[x] for x in input_configuration if input_configuration[x][2]
    }.items():
        for name, state in input_configuration.items():
            if conjunction_name in state[0]:
                conjunction_state[3][name] = False

    low_counter = 0
    high_counter = 0
    for x in range(1000):
        queue = [("broadcaster", 0, None)]
        while queue:
            (current, signal, next_point) = queue.pop(0)
            if signal:
                high_counter += 1
            else:
                low_counter += 1
            if current not in input_configuration:
                continue
            targets, is_flip_flop, is_conjunction, state = input_configuration[current]
            if is_flip_flop:
                if not signal:
                    if state:
                        input_configuration[current][3] = False
                        new_signal = 0
                    else:
                        input_configuration[current][3] = True
                        new_signal = 1
                    for target in targets:
                        queue.append((target, new_signal, current))
            elif is_conjunction:
                state[next_point] = bool(signal)
                if all(state.values()):
                    new_signal = 0
                else:
                    new_signal = 1
                for target in targets:
                    queue.append((target, new_signal, current))
            else:
                for target in targets:
                    queue.append((target, signal, current))

    result = low_counter * high_counter
    print(result)
