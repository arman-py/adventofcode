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


if __name__ == "__main__":
    rules, input_data = data.split("\n\n")
    rules = rules.split("\n")
    input_data = input_data.split("\n")
    summary = 0
    rule_dict = {}
    for rule in rules:
        rule_name, rule_body = rule.split("{")
        rule_body = rule_body[:-1].split(",")
        rule_dict[rule_name] = rule_body

    for input_line in input_data:
        rule_id = "in"
        exec(input_line[1:-1].replace(",", "\n"))
        while rule_id:
            rule_body = rule_dict[rule_id]
            for r in rule_body[:-1]:
                condition, result = r.split(":")
                if eval(condition):
                    rule_id = result
                    break
            else:
                rule_id = rule_body[-1]
            if rule_id == "A":
                summary += eval("x+m+a+s")
                break
            if rule_id == "R":
                break
    print(summary)
