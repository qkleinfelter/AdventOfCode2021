from collections import Counter
def solution():
    data = open(r'inputs\day14.in').read().strip().split('\n\n')
    print('Part 1 result: ' + str(part1(data)))
    print('Part 2 result: ' + str(part2(data)))


def part1(data):
    template = data[0]
    rules = {}
    data[1] = data[1].split('\n')
    for line in data[1]:
        pair, result = line.strip().split(' -> ')
        rules[pair] = result

    # my initial algorithm, this is not good enough for part 2, because the string will be way too large to hold in memory
    # if I wanted this could be replaced with the same algorithm from part 2, just with 10 steps instead of 40
    # start out with the template string
    string = template
    for _ in range(10):
        # the new string which we will build up
        new_string = ''
        for i in range(len(string)):
            # add the current character to the new string
            new_string += string[i]
            if i + 1 < len(string) and string[i:i+2] in rules:
                # if we can make a pair, and it is in rules, add the result of the rule to the new string
                new_string += rules[string[i:i+2]]
            # we don't need to worry about adding the second piece of the pair to the string, since it will be added in the next iteration
        # after we go through the string each time, set the string to the new string
        string = new_string
    
    # create a counter over the string
    c = Counter(string)
    # return the count of the most common character minus the count of the least common character
    return(max(c.values()) - min(c.values()))


def part2(data):
    template = data[0]
    rules = {}
    data[1] = data[1]
    for line in data[1]:
        pair, result = line.strip().split(' -> ')
        rules[pair] = result

    # better algorithm which will work for part 2 because we aren't holding the strings, just the count of each pair
    # start out with a counter that holds each pair in the template
    current = Counter()
    for i in range(len(template) - 1):
        current[template[i] + template[i+1]] += 1

    for _ in range(40):
        # create a new counter for this iteration
        new_counter = Counter()
        # loop over all of the pairs in the current counter
        for pair in current:
            if pair in rules:
                # if the pair is in the rules, we need to increment the new counter by the result of the rule
                # for example, if the pair is 'NN' and the rule is 'NN -> C'
                # then the piece of the new counter we need to increment are, NC and CN
                # this line will increment the new counter for 'NC' in this example, by the amount of the pair in the current counter
                new_counter[pair[0] + rules[pair]] += current[pair]
                # this line will increment the new counter for 'CN' in this example, by the amount of the pair in the current counter
                new_counter[rules[pair] + pair[1]] += current[pair]
        # after each time we loop through the current counter, set the current counter to the new counter
        current = new_counter
    
    # this counter will track the values of each individual character, which is what we need for the solution
    piece_counter = Counter()
    # loop over all of the pairs in the current counter
    for pair in current:
        # increment the piece counter for the first character in the pair by the amount of times that pair appeared
        piece_counter[pair[0]] += current[pair]
    # increment the piece counter for the last character in the template by 1
    piece_counter[template[-1]] += 1

    # return the count of the most common character minus the count of the least common character
    return(max(piece_counter.values()) - min(piece_counter.values()))

solution()