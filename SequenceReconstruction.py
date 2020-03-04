class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """
    def sequenceReconstruction(self, org, seqs):
        
        # write your code here
        inDegree = {}
        neighbour = {}
        
        for seq in seqs:
            for num in seq:
                if num not in inDegree:
                    inDegree[num] = 0
                    neighbour[num] = []
        
        for seq in seqs:
            for i in range(len(seq)-1):
                inDegree[seq[i+1]] += 1
                neighbour[seq[i]].append(seq[i+1])
        
        start = []
        
        if len(org) == 0 and len(inDegree) == 0:
            return True
        
        for n in inDegree:
            if inDegree[n] == 0:
                start.append(n)
        
        if len(start) != 1:
            return False
        
        queue = []
        order = []
        queue.append(start[0])
        
        while queue:
            if len(queue) > 1:
                return False
            num = queue.pop(0)
            order.append(num)
            for nei in neighbour[num]:
                inDegree[nei] -= 1
                if inDegree[nei] == 0:
                    queue.append(nei)
        
        return order == org
        
