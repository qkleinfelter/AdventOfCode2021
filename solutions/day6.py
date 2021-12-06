from collections import defaultdict
def solution():
    data = open(r'inputs\day6.in').readline().strip()
    print('Part 1 result: ' + str(part1(data)))
    print('Part 2 result: ' + str(part2(data)))


def part1(data):
    # shitty way - not efficient and won't work for the much larger list in p2
    # fish = [int(x) for x in data.split(',')]
    # for _ in range(80):
    #     for i in range(len(fish)):
    #         if fish[i] == 0:
    #             fish[i] = 6
    #             fish.append(8)
    #         else:
    #             fish[i] -= 1

    # return len(fish)
    return count_fish_after_x_days(data, 80)


def part2(data):
    return count_fish_after_x_days(data, 256)

def count_fish_after_x_days(data, x):
    fish = [int(x) for x in data.split(',')]
    # dictionary to store how many fish are at each stage
    # key is the age of the fish, value is the amount of that fish we have
    ages = defaultdict(int)
    for i in fish:
        ages[i] += 1

    # loop x times to get the fish after x days
    for _ in range(x):
        # the new set of fish ages
        new = defaultdict(int)
        # loop over all the previous ages
        for key, val in ages.items():
            # for the fish at age 0, we need to add them to the new dict at both 6 (for themselves) and 8 (for their new child)
            if key == 0:
                new[6] += val
                new[8] += val
            # otherwise, just add the fish from this age to the new dict at the age - 1
            else:
                new[key - 1] += val
        # update the ages to be the new dict
        ages = new

    # return the sum of the values, which is the total number of fish
    return sum(ages.values())

solution()