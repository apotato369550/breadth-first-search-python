# i think i get this
# x and y
# test it with another maze configuration
def create_maze():
    return [
        "O..#.",
        ".#.#.",
        "....#",
        "#...#",
        "X.###"
    ]

def create_maze_2():
    return [
        "...O##X",
        ".###...",
        ".####..",
        "...#...",
        "..###..",
        ".#.....",
        "...####"
    ]

def create_adjacency_list(maze):
    total_nodes = 0

    for row in maze:
        total_nodes += len(row)

    adjacency_list = [[] for i in range(total_nodes)]

    for row_index, row in enumerate(maze):
        for column_index, column in enumerate(row):
            # edit this to not include obstacles
            if column == "#":
                continue

            node = column_index + (row_index * len(maze[0]))

            if row_index > 0: # add top
                if maze[row_index - 1][column_index] != "#":
                    adjacency_list[node].append(column_index + ((row_index - 1) * len(maze[0])))

            if row_index < len(maze) - 1: # add bottom
                if maze[row_index + 1][column_index] != "#":
                    adjacency_list[node].append(column_index + ((row_index + 1) * len(maze[0])))

            if column_index > 0: # add to the left
                if maze[row_index][column_index - 1] != "#":
                    adjacency_list[node].append((column_index - 1) + (row_index* len(maze[0])))

            if column_index < len(maze) - 1: # add to the right
                if maze[row_index][column_index + 1] != "#":
                    adjacency_list[node].append((column_index + 1) + (row_index* len(maze[0])))

    return total_nodes, adjacency_list



        # print ""

def breadth_first_search(start, destination, predecessor, distance, adjacency_list, maze, nodes):
    queue = []
    visited = [False for x in range(nodes)]

    for i in range(nodes):
        distance[i] = [1000]
        predecessor[i] = -1

    visited[start] = True
    distance[start] = 0
    queue.append(start)

    while len(queue) != 0:
        u = queue[0]
        queue.pop(0)

        for i in range(len(adjacency_list[u])):
            if not visited[adjacency_list[u][i]]:
                # work on this
                visited[adjacency_list[u][i]] = True
                distance[adjacency_list[u][i]] = distance[u] + 1
                predecessor[adjacency_list[u][i]] = u
                queue.append(adjacency_list[u][i])

                if adjacency_list[u][i] == destination:
                    return True

    return False

def print_shortest_distance(maze):
    # start and destination coords should be like (x, y)
    nodes, adjacency_list = create_adjacency_list(maze)

    predecessor = [0 for i in range(nodes)]
    distance = [0 for i in range(nodes)]

    start = 0
    destination = 0

    for row_index, row in enumerate(maze):
        for column_index, column in enumerate(row):
            if column == "O":
                start = column_index + (row_index * len(maze[0]))
            if column == "X":
                destination = column_index + (row_index * len(maze[0]))

    print start
    print destination

    if not breadth_first_search(start, destination, predecessor, distance, adjacency_list, maze, nodes):
        print "Source and destination not connected"
        return

    path = []
    crawl = destination
    path.append(crawl)

    while predecessor[crawl] != -1:
        path.append(predecessor[crawl])
        crawl = predecessor[crawl]

    print "Shortest path length is : " + str(len(path)) + " "
    print "\nPath is: \n"

    # find a way to convert node number into coordinates (x, y)
    # use modulus?? maybe

    for i in range(len(path) - 1, -1, -1):
        coordinates = (path[i] % len(maze[0]), path[i] // len(maze[0]))
        print "Node Number: " + str(path[i]) + "  Coordinates: " + str(coordinates) + " "
        # test with other configurations
        # then try with javascript

maze = create_maze_2()

print_shortest_distance(maze)


# append up, down, left, right nodes
# do i do it per node or per coordinate??? (x, y) or n???
# return an adjacency matrix

