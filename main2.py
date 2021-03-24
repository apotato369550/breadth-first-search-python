def add_edge(source, destination):
    adjacency_list[source].append(destination)
    adjacency_list[destination].append(source)

def breadth_first_search(start, destination, predecessor, distance):
    queue = []
    visited = [False for x in range(nodes)]

    for i in range(nodes):
        distance[i] = 1000
        predecessor[i] = -1

    visited[start] = True
    distance[start] = 0
    queue.append(start)

    while len(queue) != 0:
        u = queue[0]
        queue.pop(0)

        for i in range(len(adjacency_list[u])):
            if not visited[adjacency_list[u][i]]:
                visited[adjacency_list[u][i]] = True
                distance[adjacency_list[u][i]] = distance[u] + 1
                predecessor[adjacency_list[u][i]] = u
                queue.append(adjacency_list[u][i])

                if adjacency_list[u][i] == destination:
                    return True



def print_shortest_distance(start, destination):

    predecessor = [0 for i in range(nodes)]
    distance = [0 for i in range(nodes)]

    if breadth_first_search(start, destination, predecessor, distance) == False:
        print "Source and destination are not connected"

    path = []
    crawl = destination
    path.append(crawl)

    while predecessor[crawl] != -1:
        path.append(predecessor[crawl])
        crawl = predecessor[crawl]

    print "Shortest path length is : " + str(distance[destination]) + " "
    print "\nPath is: \n"

    for i in range(len(path) - 1, -1, -1):
        print str(path[i]) + " "


# total number of nodes
nodes = 8

adjacency_list = [[] for i in range(nodes)]

# refine the thing belowVVV
# or refine the function above
add_edge(0, 3)
add_edge(0, 2)
add_edge(0, 4)
add_edge(1, 4)
add_edge(1, 5)
add_edge(2, 3)
add_edge(2, 5)
add_edge(2, 6)
add_edge(2, 7)
add_edge(4, 5)
add_edge(5, 6)
add_edge(6, 7)

for i in adjacency_list:
    print i

print_shortest_distance(7, 4)


