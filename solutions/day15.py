import heapq
from collections import defaultdict
from math import inf as INFINITY

def solution():
    data = open(r'inputs\day15.in').readlines()
    print('Part 1 result: ' + str(part1(data)))
    print('Part 2 result: ' + str(part2(data)))


def part1(data):
    # build out the grid of the risk for entering each location
    riskmap = []
    for line in data:
        riskmap.append([int(x) for x in line.strip()])

    # run dijkstra's algorithm to find the path with the lowest risk through the grid
    return dijkstra(grid=riskmap)

def part2(data):
    # build out the initial grid of the risk for entering each location
    riskmap = []
    for line in data:
        riskmap.append([int(x) for x in line.strip()])

    # width and height of each "tile", a.k.a our intial grid
    tilew = len(riskmap)
    tileh = len(riskmap[0])

    # add 4 extra tiles to the right of the grid, where each location is 1 higher risk than the same location in the tile to its left
    # looping back around to 1 if a location would go above 9
    for _ in range(4):
        for row in riskmap:
            # the tail here is the last tilew elements in the row, so we only get the most recent tile
            tail = row[-tilew:]
            # extend the row, with each square in the tail being incremented by 1 or looping back around to 1
            row.extend((x + 1) if x < 9 else 1 for x in tail)

    # add 4 extra tiles to the bottom of the grid (same increase as above)
    for _ in range(4):
        # we only want to loop over the bottom tileh rows
        for row in riskmap[-tileh:]:
            # the new row is every element in the row we are iterating over, with the increase as before
            new_row = [(x + 1) if x < 9 else 1 for x in row]
            riskmap.append(new_row)

    # run dijkstra's algorithm to find the path with the lowest risk through the grid over our new grid
    return dijkstra(grid=riskmap)

# generator function that will get the 4 neighbors of a given node
# up, down, left and right will be yielded
def neighbors4(r, c, h, w):
    for dr, dc in ((1,0), (0,1), (-1,0), (0,-1)):
        # ensure the neighbor is within the grid before yielding it
        if 0 <= r+dr < w and 0 <= c+dc < h:
            yield r+dr, c+dc

def dijkstra(grid):
    h, w = len(grid), len(grid[0])
    begin = (0, 0)
    dest = (h-1, w-1)

    # array where we will store our queue of nodes to visit, starting with the beginning node which has 0 distance and is at (0, 0)
    queue = [(0, begin)]
    # defaultdict for the minimum distance to each node that we have found, if we haven't found it yet, it will be INFINITY, and the beginning node has a distance of 0
    mindist = defaultdict(lambda: INFINITY, {begin: 0})
    # set of nodes we have already visited, so we don't bother checking them again
    visited = set()

    # while we still have nodes to visit
    while queue:
        # use heapq's min-heap priority queue to pop off the lowest distance node remaining in the queue
        dist, node = heapq.heappop(queue)

        # if this is the destination node, return its distance
        if node == dest:
            return dist
        
        # if we have already visited it, skip it
        if node in visited:
            continue

        # mark the node as visited
        visited.add(node)
        r, c = node

        # loop through its neighbors adding them to the queue if they are potentially better
        for neighbor in neighbors4(r, c, h, w):
            # ignore visited nodes
            if neighbor in visited:
                continue

            # the new distance to the neighbor is the current distance plus the risk of the neighbor
            newdist = dist + grid[neighbor[0]][neighbor[1]]
            # if the new distance is less than the smallest distance we have found to that point
            if newdist < mindist[neighbor]:
                # then update the minimum distance for that node
                mindist[neighbor] = newdist
                # and push it onto the queue using heapq's min-heap priority queue again
                heapq.heappush(queue, (newdist, neighbor))

    # if we make it here, we didn't find a path to the destination, so the result is INFINITY
    return INFINITY

solution()