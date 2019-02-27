def BFS(graph, start):
    visited = []
    queue = []
    queue.append(start)
    while queue:
        v = queue.pop(0)
        for neighbour in graph[v]:
            if neighbour not in visited and neighbour not in queue:
                queue.append(neighbour)
        visited.append(v)
    return visited


if __name__ == "__main__":
    graph = {'A': set(['B', 'C']),
             'B': set(['A', 'D', 'E']),
             'C': set(['A']),
             'D': set(['B']),
             'E': set(['B', 'F']),
             'F': set(['E'])}

    r = BFS(graph, 'A')
    print(r)
