adjacency_list = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited = []
queue = []

def breadth_first_search(visited, graph, start_node, destination):
    visited.append(start_node)
    queue.append(start_node)

    while queue:
        node = queue.pop(0)
        print(node + " ")

        if node == destination:
            return True

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

    return False

def print_shortest_distance():
    # absorb what the algorithm says in geeks for geeks
    return

# find a new tutorial that explains depth-first search in python/whatever