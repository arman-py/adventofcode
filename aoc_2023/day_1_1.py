import re


code = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""


if __name__ == "__main__":
    result = 0
    for line in code.split():
        digits = re.findall(r"\d", line)
        result += int(digits[0]) * 10 + int(digits[-1])

    print(result)
