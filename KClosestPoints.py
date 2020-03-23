"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""
import math
import heapq
class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """
    def kClosest(self, points, origin, k):
        if points == []:
            return []
        # get a list of all dists
        heap = []
        for point in points:
            heapq.heappush(heap, (-self.getDistance(origin, point), -point.x, -point.y))
            if len(heap) > k:
                heapq.heappop(heap)
        results = []
        while heap:
            dist, x, y = heapq.heappop(heap)
            results.append(Point(-x, -y))
        results.reverse()
        return results
        
        
    def getDistance(self, origin, point):
        return math.sqrt(pow((point.x - origin.x), 2) +  pow((point.y - origin.y),2))
            
