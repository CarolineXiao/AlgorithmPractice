"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""
import math
from math import pow
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
        dists = []
        for point in points:
            dist = math.sqrt(pow((point.x - origin.x), 2) +  pow((point.y - origin.y),2))
            dists.append(dist)
        # quick select -> k smallest points
        num = self.quickSelect(dists, points, 0, len(dists) - 1, k)
        print(num)
        results = []
        for i in range(len(dists)):
            if dists[i] <= num:
                results.append((dists[i], points[i].x, points[i].y))
        results = sorted(results, key = lambda x: (x[0], x[1], x[2]))
        print(results)
        r = []
        for n in results:
            r.append((n[1], n[2]))
        return r[:k]
        
    def quickSelect(self, dists, points, start, end, k):
        if start == end:
            return dists[start]
        pivot = dists[(start+end)//2]
        left = start
        right = end
        while left <= right:
            while left <= right and dists[left] < pivot:
                left += 1
            while left <= right and dists[right] > pivot:
                right -= 1
            if left <= right:
                dists[left], dists[right] = dists[right], dists[left]
                points[left], points[right] = points[right], points[left]
                left += 1
                right -= 1
        if right - start + 1 >= k:
            return self.quickSelect(dists, points, start, right, k)
        if left - start + 1 <= k:
            return self.quickSelect(dists, points, left, end, k-(left-start))
        return dists[right+1]
                    
