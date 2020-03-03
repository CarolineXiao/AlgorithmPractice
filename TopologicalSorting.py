"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        # write your code here
        nodeinDegree = self.inDegree(graph)
        start = []
        for node in nodeinDegree:
            if nodeinDegree[node] == 0:
                start.append(node)
        
        #bfs
        queue = []
        top = []
        for node in start:
            queue.append(node)
        while queue:
            my_node = queue.pop(0)
            top.append(my_node)
            for neighbors in my_node.neighbors:
                nodeinDegree[neighbors] -= 1
                if nodeinDegree[neighbors] == 0:
                    queue.append(neighbors)
    
        return top
        
        
    def inDegree(self, graph):
        nodeinDegree = {}
        for node in graph:
            nodeinDegree[node] = 0
        
        for node in graph:
            for neighbors in node.neighbors:
                nodeinDegree[neighbors] += 1
                
        return nodeinDegree
