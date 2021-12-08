import time
def solution():
    data = [int(x) for x in open(r'inputs\day7.in').read().strip().split(',')]
    start = time.time()
    print('Part 1 result: ' + str(part1(data)))
    print("Part 1 took " + str(time.time() - start) + " seconds")
    start = time.time()
    print('Part 2 result: ' + str(part2(data)))
    print("Part 2 took " + str(time.time() - start) + " seconds")
    print('Old Part 1 result: ' + str(oldp1(data)))
    print("Old Part 1 took " + str(time.time() - start) + " seconds")
    start = time.time()
    print('Old Part 2 result: ' + str(oldp2(data)))
    print("Old Part 2 took " + str(time.time() - start) + " seconds")

def part1(data):
    # not a great solution, but how I initially solved it, and it works fast enough
    # just loops through all of the locations and figures out which is the best
    # cheapest_position = (-1, 100000000)
    # for pos in range(len(data)):
    #     current_cost = 0
    #     for i in range(len(data)):
    #         crab = data[i]
    #         current_cost += abs(crab - pos)
    #     if current_cost < cheapest_position[1]:
    #         cheapest_position = (pos, current_cost)

    # return cheapest_position[1]

    # better solution, median is guaranteed to have the smallest cost to all pieces of the data,
    # so we can just sum the absolute values of the distance between every crab and the median
    data.sort()
    median = data[len(data) // 2]
    return sum(abs(x - median) for x in data)

def oldp1(data):
    cheapest_position = (-1, 100000000)
    for pos in range(len(data)):
        current_cost = 0
        for i in range(len(data)):
            crab = data[i]
            current_cost += abs(crab - pos)
        if current_cost < cheapest_position[1]:
            cheapest_position = (pos, current_cost)

    return cheapest_position[1]

def part2(data):
    # again, not a great solution but it was fast enough that this was my initial solution
    # just loops through all the locations like my first solution to p1, and determines the best using the
    # new calculate_cost function instead of just the absolute value
    # cheapest_position = (-1, 100000000)
    # for pos in range(len(data)):
    #     current_cost = 0
    #     for i in range(len(data)):
    #         crab = data[i]
    #         current_cost += calculate_cost(pos, crab)
    #     if current_cost < cheapest_position[1]:
    #         cheapest_position = (pos, current_cost)

    # return cheapest_position[1]

    # better solution, we can use the mean of the data as the best point
    # and calculate the distance from each crab to it :)
    mean = sum(data) // len(data)
    return sum(calculate_cost(crab, mean) for crab in data)

def oldp2(data):
    cheapest_position = (-1, 100000000)
    for pos in range(len(data)):
        current_cost = 0
        for i in range(len(data)):
            crab = data[i]
            current_cost += calculate_cost(pos, crab)
        if current_cost < cheapest_position[1]:
            cheapest_position = (pos, current_cost)

    return cheapest_position[1]

def calculate_cost(to, from_):
    diff = abs(to - from_)
    # initial solution, slow but works
    # cost = 0
    # for i in range(diff + 1):
    #     cost += 1 * i
    # return cost
    
    # better solution, just uses math instead of iterating to calculate the cost
    return diff * (diff + 1) // 2

solution()