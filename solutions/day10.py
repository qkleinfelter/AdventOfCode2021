from collections import deque
def solution():
    data = open(r'inputs\day10.in').readlines()
    print('Part 1 result: ' + str(part1(data)))
    print('Part 2 result: ' + str(part2(data)))

# number of points for each character for part 1
error_points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

# number of points for each character for part 2
autocomplete_points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

# closing bracket for each type
closers = {
    '{': '}',
    '[': ']',
    '(': ')',
    '<': '>'
}

def part1(data):
    # total syntax score
    syntax_score = 0
    # loop through all the lines
    for line in data:
        line = line.strip()
        # queue (that we use as a stack) to keep track of the brackets
        Q = deque()
        for c in line:
            # if its an opener, we just push it onto the stack
            if c == '{' or c == '<' or c == '(' or c == '[':
                Q.append(c)
            else:
                # otherwise, figure out which bracket we're expecting to close with, by checking the closer for the last item in the stack (popping that off at the same time)
                expected_closing = closers[Q.pop()]
                # if we didn't find the correct closing bracket, we know this line is corrupted
                if c != expected_closing:
                    # so we can simply add the score to the syntax score
                    syntax_score += error_points[c]
                    # and break out of the loop to go to the next line
                    break
    return syntax_score


def part2(data):
    # track the scores for each line
    line_scores = []
    for line in data:
        line = line.strip()
        Q = deque()
        # variable to determine if a line is corrupt or not
        corrupt = False
        for c in line:
            # just like before push openers onto the stack
            if c == '{' or c == '<' or c == '(' or c == '[':
                Q.append(c)
            else:
                # and pop off the item to check the expected closing bracket
                expected_closing = closers[Q.pop()]
                if c != expected_closing:
                    # this time, we ignore this line because its corrupted
                    corrupt = True
        # if its corrupt, we can just continue onto the next line
        if corrupt:
            continue
        # now we've popped down to the end of the line and we know its not corrupt

        # track the line score for this line
        line_score = 0
        # while we still have stuff on the stack (all openers)
        while Q:
            # pop off the last item
            c = Q.pop()
            # multiply the score by 5
            line_score *= 5
            # get the closer for the last item
            closer = closers[c]
            # and add to the line score the amount of points for the closer
            line_score += autocomplete_points[closer]
        # then add the line score to the list
        line_scores.append(line_score)

    # sort the scores
    line_scores.sort()
    # and return the middle score as the solution
    return line_scores[len(line_scores) // 2]

solution()