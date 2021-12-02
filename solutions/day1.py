def solution():
    data = [int(x) for x in open(r'inputs\day1.in')]
    print('Part 1 result: ' + str(part1(data)))
    print('Part 2 result: ' + str(part2(data)))

def part1(data):
    sum = 0
    for i, val in enumerate(data):
        if i == 0:
            continue
        else:
            if val > data[i-1]:
                sum += 1
    return sum

def part2(data):
    sum = 0
    for i, val in enumerate(data):
        if len(data) < i+4:
            break
        three_window_sum = val + data[i+1] + data[i+2]
        next_sum = data[i+1] + data[i+2] + data[i+3]
        if next_sum > three_window_sum:
            sum += 1
    return sum

solution()