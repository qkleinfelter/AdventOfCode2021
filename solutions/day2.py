def solution():
    data = open(r'inputs\day2.in').readlines()
    print('Part 1 result: ' + str(part1(data)))
    print('Part 2 result: ' + str(part2(data)))


def part1(data):
    horiz = 0
    depth = 0
    for line in data:
        pieces = line.split()
        dir = pieces[0]
        amt = int(pieces[1])
        if dir == "forward":
            horiz += amt
        elif dir == "up":
            depth -= amt
        elif dir == "down":
            depth += amt
    return horiz * depth


def part2(data):
    horiz = 0
    depth = 0
    aim = 0
    for line in data:
        pieces = line.split()
        dir = pieces[0]
        amt = int(pieces[1])
        if dir == "forward":
            horiz += amt
            depth += aim * amt
        elif dir == "up":
            aim -= amt
        elif dir == "down":
            aim += amt
    
    return horiz * depth

solution()