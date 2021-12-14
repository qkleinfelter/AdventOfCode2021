def solution():
    data = open(r'inputs\day13.in').readlines()
    print('Part 1 result: ' + str(part1(data)))
    print('Part 2 result: ' + str(part2(data)))


def part1(data):
    # build out the grid and instructions from our data
    grid, fold_instructions = build_grid_and_instructions(data)
    # run the first fold only
    grid = fold(grid, fold_instructions[0])

    # the length of the grid is our answer
    return len(grid)

def part2(data):
    # build out the grid and instructions from our data
    grid, fold_instructions = build_grid_and_instructions(data)

    # loop through every fold instruction, running it
    for i in range(len(fold_instructions)):
        instr = fold_instructions[i]
        grid = fold(grid, instr)

    # get the max x and y values
    X = max([x for (x,y) in grid.keys()]) + 1
    Y = max([y for (x,y) in grid.keys()]) + 1

    # print out the word by looping through the grid printing one row at a time
    ans = ''
    for y in range(Y):
        for x in range(X):
            ans += ('x' if (x,y) in grid else ' ')
        print(ans)
        ans = ''

    return 'Read above'

def build_grid_and_instructions(data):
    grid = {}
    fold_instructions = []
    for line in data:
        line = line.strip()
        # ignore the blank lines
        if line == '':
            continue
        if line.startswith('fold'):
            # split on the equals sign
            a, b = line.split('=')
            # now, split the first piece on the comma and take the third element, this is our axis
            a = a.split(' ')[2]
            # add the instruction as a tuple to our fold_instructions list, for example fold along y=3 would be ('y', 3)
            fold_instructions.append((a, b))
        else:
            # split on the comma and cast both to ints
            x, y = [int(x) for x in line.strip().split(',')]
            # set that spot in our grid to be true
            grid[(x, y)] = True

    # return the grid & instructions
    return grid, fold_instructions

def fold(grid, instruction):
    grid2 = {}
    # the line we want to fold along
    fold_line = int(instruction[1])
    if instruction[0] == 'x':
        for (x, y) in grid:
            # if our x value is less than the fold line, we leave it alone, and copy the same location to the new grid
            if x < fold_line:
                grid2[(x, y)] = True
            else:
                # otherwise, we need the new location to be flipped across the fold line,
                # so its new x value is the fold line minus the distance between the fold line and the current x value
                # i.e. an x of 7 folded over 5 would get moved to x = 3
                grid2[((fold_line - (x - fold_line), y))] = True
    else:
        # if it isn't x, it must be y
        assert instruction[0] == 'y'
        for (x, y) in grid:
            # if our y value is less than the fold line, we leave it alone, and copy the same location to the new grid
            if y < fold_line:
                grid2[(x, y)] = True
            else:
                # otherwise, we need the new location to be flipped across the fold line,
                # same logic as above, but with y instead
                grid2[((x, fold_line - (y - fold_line)))] = True

    # return the new grid
    return grid2

solution()