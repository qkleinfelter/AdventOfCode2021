def solution():
    data = open(r'inputs\day11.in').readlines()
    print('Part 1 result: ' + str(part1(data)))
    print('Part 2 result: ' + str(part2(data)))

def part1(data):
    # 2d array of ints that represents the octopus' current value
    octomap = []
    for line in data:
        octomap.append([int(x) for x in line.strip()])
    
    adj = {
            # up one row all 3 spots
            (-1, 1),
            (-1, 0),
            (-1, -1),

            # same row, left and right spots
            (0, -1),
            (0, 1),

            # down 1 row, all 3 spots
            (1, -1),
            (1, 0),
            (1, 1)
        }
    # track the number of flashes
    flash_count = 0
    rows = len(octomap)
    cols = len(octomap[0])

    # 100 steps for p1
    for step in range(100):
        # get the new octomap by adding 1 to each value
        octomap = [[x + 1 for x in row] for row in octomap]
        # our stack is a list which consists of a tuple of the row and column of each value that is greater than 9, a.k.a the spots a flash should occur at
        stack = [(row, col) for row in range(rows) for col in range(cols) if octomap[row][col] > 9]

        # while we have stuff in the stack
        while stack:
            # pop off the top value into our row and column variables
            row, col = stack.pop()
            # increment our flash count
            flash_count += 1
            # loop through the neighbors of the popped value
            for dx, dy in adj:
                if 0 <= row + dx < rows and 0 <= col + dy < cols:
                    # if its a valid neighbor, add 1 to it, and if it is now a 10, add it to the stack
                    octomap[row + dx][col + dy] += 1
                    if octomap[row + dx][col + dy] == 10:
                        stack.append((row + dx, col + dy))

        # at the end of each step, set all values greater than 9 to 0, because they flashed that step
        octomap = [[0 if x > 9 else x for x in row] for row in octomap]

    return flash_count


def part2(data):
    # 2d array of ints of the octopus' current value
    octomap = []
    for line in data:
        octomap.append([int(x) for x in line.strip()])

    adj = {
            # up one row all 3 spots
            (-1, 1),
            (-1, 0),
            (-1, -1),

            # same row, left and right spots
            (0, -1),
            (0, 1),

            # down 1 row, all 3 spots
            (1, -1),
            (1, 0),
            (1, 1)
        }
    rows = len(octomap)
    cols = len(octomap[0])
    # similar setup to part 1, but now we track the number of steps outside the loop and use an infinite while loop, since we don't know when the synchronized flash will occur
    step = 0
    while True:
        step += 1
        octomap = [[x + 1 for x in row] for row in octomap]
        stack = [(row, col) for row in range(rows) for col in range(cols) if octomap[row][col] > 9]

        # count the number of flashes in the current step
        step_flashes = 0
        while stack:
            row, col = stack.pop()
            # each time we pop off the stack, we are doing a flash, so increment our flash count
            step_flashes += 1
            for dx, dy in adj:
                if 0 <= row + dx < rows and 0 <= col + dy < cols:
                    octomap[row + dx][col + dy] += 1
                    if octomap[row + dx][col + dy] == 10:
                        stack.append((row + dx, col + dy))

        octomap = [[0 if x > 9 else x for x in row] for row in octomap]
        # if we have 100 flashes this step, then all of the octopi have flashed, because there is a 10x10 grid of octopi, and each octopus flashes at most once per step
        if step_flashes == 100:
            # so return the step we are on as they are synchronized here
            return step

solution()