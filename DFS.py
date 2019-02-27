def DFS(graph, start):
    visited = []
    visited.append(start)
    DFS_visit(graph, start, visited)
    return visited

def DFS_visit(graph, node, visited):
    for v in graph[node]:
        if v not in visited:
            visited.append(v)
            DFS_visit(graph, v, visited)

if __name__ == "__main__":
    graph = {'A': set(['B', 'C']),
             'B': set(['A', 'D', 'E']),
             'C': set(['A']),
             'D': set(['B']),
             'E': set(['B', 'F']),
             'F': set(['E'])}
    r = DFS(graph, 'D')
    print(r)
