# i think i get this
# x and y
# it's a start
def create_maze():
    return [
        "O..#.",
        ".#.#.",
        "....#",
        "#...#",
        "X.###"
    ]

def create_adjacency_list(maze):
    total_nodes = 0

    for row in maze:
        for column in row:
            total_nodes += 1

    adjacency_list = [[] for i in range(total_nodes)]

    for row_index, row in enumerate(maze):
        for column_index, column in enumerate(row):
            # print maze[row_index][column_index],
            node = column_index + (row_index * len(maze[0]))

            if row_index > 0: # add top
                adjacency_list[node].append(column_index + ((row_index - 1) * len(maze[0])))

            if row_index < len(maze) - 1: # add bottom
                adjacency_list[node].append(column_index + ((row_index + 1) * len(maze[0])))

            if column_index > 0: # add to the left
                adjacency_list[node].append((column_index - 1) + (row_index* len(maze[0])))

            if column_index < len(maze) - 1: # add to the right
                adjacency_list[node].append((column_index + 1) + (row_index* len(maze[0])))

    for node in adjacency_list:
        print node


        # print ""

def breadth_first_search(start, destination, predecessor, distance, maze):
    return

def print_shortest_distance(start, destination, maze):
    return

maze = create_maze()
create_adjacency_list(maze)


# append up, down, left, right nodes
# do i do it per node or per coordinate??? (x, y) or n???
# return an adjacency matrix

