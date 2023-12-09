data = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""


if __name__ == "__main__":
    split_data = data.split("\n")
    result = 0
    for line in split_data:
        report = [int(x) for x in line.split()]
        new_report = []
        last_values = []
        while report:
            a = report.pop(0)
            if report:
                new_report.append(report[0]-a)
            else:
                last_values.append(a)
                report = new_report
                new_report = []
            if all(v == 0 for v in report):
                break
        nex_value = 0
        for x in last_values[::-1]:
            nex_value += x
        result += nex_value
    print(result)
