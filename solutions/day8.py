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
    signals = []
    outputs = []
    output_sum = 0
    for line in data:
        line = line.split("|")
        signals.append(line[0].split())
        outputs.append(line[1].split())

    # loop over all the signals and outputs
    for signal, output in zip(signals, outputs):
        # variable to track which string indicates the digit
        # i.e. if ab indicates 1, then mapping[1] == "ab"
        mapping = ['' for i in range(10)]
        # sort the signal by the length of the pieces
        signal = sorted(signal, key=len)
        for i in signal:
            # 1, 7 and 4 always have length 2, 3, and 4 respectively
            if   len(i) == 2: mapping[1] = i
            elif len(i) == 3: mapping[7] = i
            elif len(i) == 4: mapping[4] = i
            # 3, 5, and 2 are the options for length 5 strings
            elif len(i) == 5:
                # if all of the pieces in the mapping for 1 are in the digit, then it must be a 3
                if    all([c in i for c in mapping[1]]): mapping[3] = i
                # if we have 3 pieces of the mapping for 4 in the digit, then it must be a 5
                elif  sum([c in i for c in mapping[4]]) == 3: mapping[5] = i
                # otherwise, its a 2
                else: mapping[2] = i
            # 9, 0, and 6 are the options for 6 length strings
            elif len(i) == 6: 
                # if all of the pieces in the mapping for 4 are in the digit, then it must be a 9
                if    all([c in i for c in mapping[4]]): mapping[9] = i
                # if all of the pieces in the mapping for 7 are in the digit, then it must be a 0
                elif  all([c in i for c in mapping[7]]): mapping[0] = i
                # otherwise, its a 6
                else: mapping[6] = i
            # there is only 1 more string remaining at 7 length, which must be an 8
            elif len(i) == 7: mapping[8] = i
            else: throw(f"Error: invalid digit length on digit: {i}")

        output_number = 0
        # loops through the output pieces
        for j, n in enumerate(output[::-1]):
            # check the current digit vs the mapping for all 10 digits
            for i in range(10):
                # if all of the pieces of the mapping are in the number, and the length of the mapping matches the length of the number
                if all([c in n for c in mapping[i]]) and len(mapping[i]) == len(n):
                    # then we have found the digit, so add it to the output number in the appropriate slot
                    output_number += i * 10 ** j
                    break
        # once we've got the number, add it to the sum
        output_sum += int(output_number)

    return output_sum

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