# Source : https://leetcode.com/problems/merge-intervals/description/

# Algo/DS : Array

# Complexity : O(n log n)

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if intervals == []: return intervals
        intervals.sort(key = lambda x : x.start)
        result = [intervals[0]]
        n  = len(intervals)
        for i in range(1, n):
            if result[-1].end >= intervals[i].start : 
                result[-1].end = max(result[-1].end, intervals[i].end)
            elif result[-1].start == intervals[i].start and result[-1].end == intervals[i].end and i < n - 1 :
                continue
            else:
                result.append(intervals[i])
        return result
        