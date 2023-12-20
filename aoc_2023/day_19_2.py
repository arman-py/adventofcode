data = """px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}"""


import copy


def range_calculator(ranges, rule_key):
    if rule_key == "A":
        return [ranges]
    if rule_key == "R":
        return []
    final_ranges = []
    for rule_body in rule_dict[rule_key]:
        if ":" in rule_body:
            condition, destination = rule_body.split(":")
            sign = "<" if "<" in condition else ">"
            variable_name, target = condition.split(sign)
            target = int(target)
            rang = ranges[variable_name]
            if sign == "<":
                if rang[0] >= target:
                    continue
                new_ranges = copy.copy(ranges)
                new_ranges[variable_name] = (rang[0], min(rang[1], target - 1))
                final_ranges.extend(range_calculator(new_ranges, destination))
                new_ranges_2 = copy.copy(ranges)
                new_ranges_2[variable_name] = (max(rang[0], target), rang[1])
                ranges = new_ranges_2
            elif sign == ">":
                if rang[1] <= target:
                    continue
                new_ranges = copy.copy(ranges)
                new_ranges[variable_name] = (max(rang[0], target + 1), rang[1])
                final_ranges.extend(range_calculator(new_ranges, destination))
                new_ranges_2 = copy.copy(ranges)
                new_ranges_2[variable_name] = (rang[0], min(rang[1], target))
                ranges = new_ranges_2
        else:
            final_ranges.extend(range_calculator(ranges, rule_body))
    return final_ranges


if __name__ == "__main__":
    rules, _ = data.split("\n\n")
    rules = rules.split("\n")
    rule_dict = {}
    for rule in rules:
        rule_name, body = rule.split("{")
        body = body[:-1].split(",")
        rule_dict[rule_name] = body
    start = "in"
    all_ranges = {
        "x": (1, 4000),
        "m": (1, 4000),
        "a": (1, 4000),
        "s": (1, 4000)
    }
    calculated = range_calculator(all_ranges, start)
    summary = 0
    for calculated_range in calculated:
        result = 1
        for variable in calculated_range:
            length = calculated_range[variable][1] - calculated_range[variable][0] + 1
            result *= length
        summary += result
    print(summary)
