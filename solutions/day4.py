def solution():
    data = [x for x in open(r'inputs\day4.in').read().strip().split("\n")]
    number_order = open(r'inputs\day4.in').readline().strip().split(',')
    print('Part 1 result: ' + str(part1(data, number_order)))
    print('Part 2 result: ' + str(part2(data, number_order)))


def part1(data, number_order):
    # clean up data
    data = data[2:]
    data = [x for x in data if x != '']
    board_count = int(len(data) / 5)

    # fill out the boards
    boards = []
    for i in range(board_count):
        board = []
        for x in range(5):
            row = [int(num) for num in data[i * 5 + x].split()]
            board.append(row)
        boards.append(board)

    for i in range(len(number_order)):
        # loop through all the numbers in the list
        current_number = number_order[i]
        # check each board
        for board in boards:
            # loop through each row looking for the current number
            for rowindex in range(5):
                row = board[rowindex]
                for colindex in range(5):
                    # if we have the number, mark it by replacing it with -1, since we don't need the number later
                    # and all numbers in the bingo game must be positive
                    if row[colindex] == int(current_number):
                        row[colindex] = -1

                        # cannot be any bingos if less than 5 numbers have been called
                        if (i < 5):
                            continue
                        # since we've just marked a number we need to check if we have a bingo
                        if has_bingo(board):
                            unmarked = 0
                            # sum the unmarked numbers
                            for j in range(5):
                                for k in range(5):
                                    if (board[j][k] != -1):
                                        unmarked += board[j][k]
                            # return the sum of the unmarked numbers multiplied by the current number for our solution
                            return unmarked * int(current_number)

    # if we get here, we didn't find a bingo, and something went wrong so return -1
    return -1

def part2(data, number_order):
    # clean up data
    data = data[2:]
    data = [x for x in data if x != '']
    board_count = int(len(data) / 5)

    # fill out the boards
    boards = []
    for i in range(board_count):
        board = []
        for x in range(5):
            row = [int(num) for num in data[i * 5 + x].split()]
            board.append(row)
        boards.append(board)

    # track the winning boards in this dictionary, key is the index of the board in boards, value is the sum of the unmarked numbers multiplied by the number that was called when it won
    winning_boards = {}
    # track the most recent winning board
    last_win_index = -1
    for i in range(len(number_order)):
        # loop through all the numbers in the list
        current_number = number_order[i]
        for boardindex, board in enumerate(boards):
            # if we have already won on this board, we don't care about it so skip it
            if boardindex in winning_boards:
                continue
            for rowindex in range(5):
                row = board[rowindex]
                for colindex in range(5):
                    if row[colindex] == int(current_number):
                        row[colindex] = -1
                        # cannot be any bingos if less than 5 numbers have beencalled
                        if (i < 5):
                            continue
                        if has_bingo(board):
                            unmarked = 0
                            for j in range(5):
                                for k in range(5):
                                    if (board[j][k] != -1):
                                        unmarked += board[j][k]
                            # if we have a bingo, add it to the winning boards dictionary
                            winning_boards[boardindex] = unmarked * int(current_number)
                            # and store this board as the most recent winning board
                            last_win_index = boardindex

    # return the score of the final winning board as our solution
    return winning_boards[last_win_index]


def has_bingo(board):
    # check each row
    for row in board:
        # if the sum of the row is -5 then its a bingo since we're marking spots with -1 when its been called
        if sum(row) == -5:
            return True
    # check each column
    for col in range(5):
        # make sure all 5 spots in the column are -1
        if (board[0][col] == board[1][col] == board[2][col] == board[3][col] == board[4][col] == -1):
            return True
    # if we made it here, there is no bingo
    return False

solution()