"""
class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""

class Solution:
    """
    @param node: A undirected graph node
    @return: A undirected graph node
    """
    def cloneGraph(self, node):
        # write your code here
        # 1. use bfs to get all the nodes
        # 2. store all old -> new mappings
        # 3. copy all the neighbours accodring to the mappings
        
        if node == None:
            return None
        
        nodes = self.getNodes(node)
        
        mapping = {}
        for n in nodes:
            mapping[n] = Node(n.val)
        
        for n in nodes:
            new_node = mapping[n]
            for neighbor in n.neighbors:
                new_neighbor = mapping[neighbor]
                new_node.neighbors.append(new_neighbor)
            
        return mapping[node]
        
        
    def getNodes(self, node):
        queue = []
        queue.append(node)
        nodes = set()
        nodes.add(node)
        
        while queue:
            my_node = queue.pop(0)
            for n in my_node.neighbors:
                if n not in nodes:
                    nodes.add(n)
                    queue.append(n)
        
        return nodes
            
            
