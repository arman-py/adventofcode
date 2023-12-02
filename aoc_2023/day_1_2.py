import re


code = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""


if __name__ == "__main__":
    result = 0
    help_dict = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }
    for line in code.split():
        for word, number in help_dict.items():
            line = line.replace(word, f"{word[:2]}{number}{word[2:]}")
        digits = re.findall(r"\d", line)
        result += int(digits[0]) * 10 + int(digits[-1])

    print(result)