def solution():
    data = [x.strip() for x in open(r'inputs\day5.in').readlines()]
    print('Part 1 result: ' + str(part1(data)))
    print('Part 2 result: ' + str(part2(data)))


def part1(data):
    # generically sized locs array of 1000x1000, could be improved by determining the actual size needed
    locs = [[0 for _ in range(1000)] for _ in range(1000)]
    # loop through all the lines
    for line in data:
        # splits the line out into the appropriate variables
        left, right = line.split('->')
        x1, y1 = left.split(',')
        x2, y2 = right.split(',')
        # calculate the difference in x and y, a.k.a the direction of the line
        dx = int(x2) - int(x1)
        dy = int(y2) - int(y1)
        # ignore diagonal lines for part 1
        if dx != 0 and dy != 0:
            continue
        # horizontal lines
        if dx != 0:
            # start at x1
            currentx = int(x1)
            # loop until we are at x2
            while currentx != int(x2):
                # increase the current spots count by 1
                locs[int(y1)][currentx] += 1
                # if we're moving in the positive direction, increase the currentx by 1
                if dx > 0:
                    currentx += 1
                # if we're moving in the negative direction, decrease the currentx by 1
                else:
                    currentx -= 1
            # increase our current location by 1 to make sure the final location is counted
            locs[int(y1)][currentx] += 1

        # vertical lines
        if dy != 0:
            # start at y1
            currenty = int(y1)
            # loop until we are at y2
            while currenty != int(y2):
                # increase the current spots count by 1
                locs[currenty][int(x1)] += 1
                # if we're moving in the positive direction, increase the currenty by 1
                if dy > 0:
                    currenty += 1
                # if we're moving in the negative direction, decrease the currenty by 1
                else:
                    currenty -= 1
            # increase our current location by 1 to make sure the final location is counted
            locs[currenty][int(x1)] += 1
            
    # loop through all the locations and count the number of times a spot has been used more than once
    overlap_points = 0
    for x in range(1000):
        for y in range(1000):
            if locs[x][y] > 1:
                overlap_points += 1
    # the count of spots used more than once is our solution
    return overlap_points

def part2(data):
    locs = [[0 for _ in range(1000)] for _ in range(1000)]
    for line in data:
        left, right = line.split('->')
        x1, y1 = left.split(',')
        x2, y2 = right.split(',')
        dx = int(x2) - int(x1)
        dy = int(y2) - int(y1)
        # horizontal lines
        if dx != 0 and dy == 0:
            currentx = int(x1)
            while currentx != int(x2):
                locs[int(y1)][currentx] += 1
                if dx > 0:
                    currentx += 1
                else:
                    currentx -= 1
            locs[int(y1)][currentx] += 1
        # vertical lines
        elif dy != 0 and dx == 0:
            currenty = int(y1)
            while currenty != int(y2):
                locs[currenty][int(x1)] += 1
                if dy > 0:
                    currenty += 1
                else:
                    currenty -= 1
            locs[currenty][int(x1)] += 1
        # diagonal lines
        else:
            # need to track both x and y here
            currentx, currenty = int(x1), int(y1)
            # loop until we're at the desired location
            while currentx != int(x2) and currenty != int(y2):
                # increase the current spots count by 1
                locs[currenty][currentx] += 1
                # adjust both x and y depending on the delta
                if dx > 0:
                    currentx += 1
                else:
                    currentx -= 1
                if dy > 0:
                    currenty += 1
                else:
                    currenty -= 1
            # make sure we count the last spot
            locs[currenty][currentx] += 1

    # count the number of times a spot has been used more than once
    overlap_points = 0
    for x in range(1000):
        for y in range(1000):
            if locs[x][y] > 1:
                overlap_points += 1
    # return the solution
    return overlap_points

solution()