data = """..."""


from math import lcm


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
    four_conjunctions = {}
    low_counter = 0
    high_counter = 0
    for x in range(1, 100000000):
        queue = [("broadcaster", 0, None)]
        if x % 10000 == 0:
            cycles = []
            for name, values in four_conjunctions.items():
                cycles.append(values[1]-values[0])
            print(lcm(*cycles))
            break

        while queue:
            (current, signal, next_point) = queue.pop(0)

            # IMPORTANT: list below is specified for my example conjunctions that can change &ft -> rx
            
            if current in ["vz", "bq", "qh", "lt"] and not signal:
                if current in four_conjunctions:
                    four_conjunctions[current].append(x + 1)
                else:
                    four_conjunctions[current] = [x + 1]
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
