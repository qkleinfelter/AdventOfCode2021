def solution():
    data = open(r'inputs\day8.in').readlines()
    print('Part 1 result: ' + str(part1(data)))
    print('Part 2 result: ' + str(part2(data)))


def part1(data):
    uniques = 0
    for line in data:
        output = line.split("|")[1]
        digits = output.split()
        for digit in digits:
            if is_unique(digit) != -1:
                uniques += 1
    return uniques


def part2(data):
    output_sum = 0
    for line in data:
        input, output = line.split("|")
        indigits = input.split()
        outdigits = output.split()

def is_unique(digit):
    if len(digit) == 2:
        return 1
    elif len(digit) == 3:
        return 7
    elif len(digit) == 4:
        return 4
    elif len(digit) == 7:
        return 8
    else:
        return -1

solution()