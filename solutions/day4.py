def solution():
    data = [x for x in open(r'inputs\test.in').read().strip().split("\n")]
    number_order = open(r'inputs\test.in').readline().strip().split(',')
    print('Part 1 result: ' + str(part1(data, number_order)))
    print('Part 2 result: ' + str(part2(data)))


def part1(data, number_order):
    data = data[2:]
    data = [x for x in data if x != '']
    board_count = int(len(data) / 5)
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
        for board in boards:
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
            print(unmarked, current_number)
            return unmarked * int(current_number)

    return 0

def part2(data):
    return 0


def has_bingo(board):
    for row in board:
        if sum(row) == -5:
            return True
    for col in range(5):
        if (board[0][col] == board[1][col] == board[2][col] == board[3][col] == board[4][col] == -1):
            return True
    return False

solution()