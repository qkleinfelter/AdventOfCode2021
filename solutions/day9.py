from collections import deque
def solution():
    data = open(r'inputs\day9.in').readlines()
    print('Part 1 result: ' + str(part1(data)))
    print('Part 2 result: ' + str(part2(data)))


def part1(data):
    # build the heightmap as a 2d array of ints
    heightmap = []
    for line in data:
        line = line.strip()
        row = []
        for c in line:
            row.append(int(c))
        heightmap.append(row)

    # (dx, dy) for each adjacent cell (not checking diagonals)
    checks = {
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    }

    # variable to hold the answer
    lowscore = 0
    rows = len(heightmap)
    cols = len(heightmap[0])

    # loop through the whole 2d array
    for row in range(rows):
        for col in range(cols):
            # value of the current cell
            value = heightmap[row][col]
            # list of the adjacent values
            adjacent_spots = []
            # loop through the checks
            for dx, dy in checks:
                # calculate the new row and column by adding dx and dy to the current value
                new_row = row + dx
                new_col = col + dy
                # if the new row and column are in bounds
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    # add the spot to the adjacent spots list
                    adjacent_spots.append(heightmap[new_row][new_col])
            # if all of the adjacent spots are strictly greater than the current cell's value
            if all(adj > value for adj in adjacent_spots):
                # then add the current cell's value + 1 to the lowscore
                lowscore += 1 + value
    # return the total lowscore which is the solution
    return lowscore

def part2(data):
    heightmap = []
    for line in data:
        line = line.strip()
        row = []
        for c in line:
            row.append(int(c))
        heightmap.append(row)

    checks = {
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    }

    # list of all of the basin sizes
    basin_sizes = []
    # set of all the seen locations, stored as (row, col) tuples
    SEEN = set()
    rows = len(heightmap)
    cols = len(heightmap[0])

    # loop through the whole 2d array
    for row in range(rows):
        for col in range(cols):
            # if we haven't already seen this spot & it is not a 9
            if (row, col) not in SEEN and heightmap[row][col] != 9:
                # create a new basin, and store its size in basin_size
                basin_size = 0
                # setup a queue for the breadth-first search
                queue = deque()
                # start the queue with the current spot
                queue.append((row, col))
                # while we have stuff in the queue
                while queue:
                    # new spot is the first thing in the queue
                    row, col = queue.popleft()
                    # if we've already seen this spot, skip it
                    if (row, col) in SEEN:
                        continue
                    # add the spot to the seen set
                    SEEN.add((row, col))
                    # and increase the basin size by 1
                    basin_size += 1
                    # simialrly to part 1, loop through the checks, to potentially add the adjacent spots to the basin
                    for dx, dy in checks:
                        new_row = row + dx
                        new_col = col + dy
                        # if the new row and column are in bounds and the new spot isn't a 9
                        if 0 <= new_row < rows and 0 <= new_col < cols and heightmap[new_row][new_col] != 9:
                            # add it to the queue to be processed
                            queue.append((new_row, new_col))

                # now that we've finished processing this basin, add its size to the list of basin sizes
                basin_sizes.append(basin_size)
    # sort the basin sizes
    basin_sizes.sort()
    # return the product of the top 3 basin sizes (the last 3 in the sorted list)
    return basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3]

solution()