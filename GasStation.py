class Solution:
    """
    @param gas: An array of integers
    @param cost: An array of integers
    @return: An integer
    """
    def canCompleteCircuit(self, gas, cost):
        if gas == [] or gas == None or cost == None or cost == []:
            return -1
        
        index = 0
        curSum = 0
        total = 0
        
        for i in range(len(gas)):
            curSum += gas[i] - cost[i]
            total += gas[i] - cost[i]
            if curSum < 0:
                index = i+1
                curSum = 0
        
        if total < 0:
            return -1
        return index
