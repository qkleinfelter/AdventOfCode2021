from collections import defaultdict, deque
graph = defaultdict(list)
def solution():
    global graph
    data = open(r'inputs\day12.in').readlines()
    for line in data:
        start, end = line.strip().split('-')
        graph[start] += [end]
        graph[end] += [start]
    print('Part 1 result: ' + str(part1(data)))
    print('Part 2 result: ' + str(part2(data)))

def part1(data):
    return solve(part1=True)

def part2(data):
    return solve(part1=False)

# iterates through all the valid paths, dependent on which part we're doing
def solve(part1):
    global graph
    # tuple for our queue, keeps track of where we are, what small caves we have visited, and if we have visited a small cave twice yet or not
    start = ('start', set(['start']), False)
    # track our number of valid paths for the answer
    num_valid_paths = 0
    # start our queue with the beginning tuple
    queue = deque([start])
    while queue:
        # pop the left most item off the queue into the variables
        current, visited_small, twice = queue.popleft()
        # can't visit end twice, so just add one to our valid paths and continue on to the next step of the queue
        if current == 'end':
            num_valid_paths += 1
            continue
        # if we aren't at the end, loop through all neighbors of the current node
        for neighbor in graph[current]:
            # if its not in our list of small caves we've already visited
            if neighbor not in visited_small:
                # a new set for the small caves, starting with the current one
                new_small = set(visited_small)
                # add the neighbor to the set if its also a small cave
                if neighbor.islower():
                    new_small.add(neighbor)
                # add this neighbor to the queue with the appropriate small cave set, and whether or not we've used up our second visit to a small cave yet
                queue.append((neighbor, new_small, twice))
            # otherwise, if the neighbor is in visited_small, we haven't used our second visit yet, its not the start or end, and we're doing part 2
            elif neighbor in visited_small and twice is False and neighbor not in ['start', 'end'] and not part1:
                # add the neighbor to the queue, with the same visited small set, but set twice to true
                queue.append((neighbor, visited_small, True))
    # return the number of valid paths, our solution
    return num_valid_paths

solution()