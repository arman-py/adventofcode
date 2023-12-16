data = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"


if __name__ == "__main__":
    split_data = data.split(',')
    result = 0
    for line in split_data:
        line_value = 0
        for elem in line:
            line_value += ord(elem)
            line_value *= 17
            line_value = line_value % 256

        result += line_value
    print(result)
