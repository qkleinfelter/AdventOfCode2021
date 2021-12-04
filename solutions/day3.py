from collections import Counter

def solution():
    data = [x for x in open(r'inputs\day3.in').read().strip().split("\n")]
    print('Part 1 result: ' + str(part1(data)))
    print('Part 2 result: ' + str(part2(data)))

def part1(data):
    gamma = ""
    epsilon = ""

    for i in range(len(data[0])):
        # counts the amount of times each character appears at this bit in data
        common = Counter([x[i] for x in data])

        # more common bit goes into gamma, less common bit goes into epsilon
        if common['0'] > common['1']:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"
    
    # convert gamma and epsilon from binary to decimal, and multiply for result
    return int(gamma, 2) * int(epsilon, 2)


def part2(data):
    oxygen = ""
    co2 = ""

    for i in range(len(data[0])):
        # counts the amount of times each character appears at this bit in data
        common = Counter([x[i] for x in data])

        if common['0'] > common['1']:
            # only keep pieces of data if there is a 0 at the current bit, since it is the most common here
            data = [x for x in data if x[i] == '0']
        else:
            # only keep pieces of data if there is a 1 at the current bit, since it is the most common here
            data = [x for x in data if x[i] == '1']
        # stop when we only have 1 piece remaining
        if len(data) == 1:
            oxygen = data[0]
            break

    data = [x for x in open(r'inputs\day3.in').read().strip().split("\n")]
    for i in range(len(data[0])):
        # counts the amount of times each character appears at this bit in data
        common = Counter([x[i] for x in data])

        if common['0'] > common['1']:
            # only keep pieces of data if there is a 0 at the current bit, since it is the least common here
            data = [x for x in data if x[i] == '1']
        else:
            # only keep pieces of data if there is a 1 at the current bit, since it is the least common here
            data = [x for x in data if x[i] == '0']
        # stop when we only have 1 piece remaining
        if len(data) == 1:
            c02 = data[0]
            break
    
    # convert oxygen and c02 from binary to decimal, and multiply for result
    return (int(oxygen, 2) * int(c02, 2))

solution()