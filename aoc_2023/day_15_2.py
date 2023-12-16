data = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"


if __name__ == "__main__":
    split_data = data.split(',')
    new_list = [{} for i in range(256)]
    for line in split_data:
        if "=" in line:
            line, numb = line.split("=")
            numb = int(numb)
            line_hash = calculate_hash(line)
            new_list[line_hash][line] = numb
        else:
            line = line[:-1]
            line_hash = calculate_hash(line)
            if line in new_list[line_hash]:
                new_list[line_hash].pop(line)
    result = 0
    for index, row in enumerate(new_list):
        for slot, item in enumerate(row):
            result += (index+1) * (slot+1) * row[item]
    print(result)
