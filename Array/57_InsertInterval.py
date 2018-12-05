# Source : https://leetcode.com/problems/insert-interval/description/

# Algo/DS : Interval

# Complexity : O(n)

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        
        res = []
        
        i = 0
        # # skip smaller parts
        while i < len(intervals) and intervals[i].end < newInterval.start:
            res.append(intervals[i])
            i += 1
        
        ## merge
        while i < len(intervals) and intervals[i].start <= newInterval.end:
            newInterval.start = min(newInterval.start, intervals[i].start)
            newInterval.end = max(newInterval.end, intervals[i].end)
            i += 1
        res.append(newInterval)
            
        # add the rest
        while i < len(intervals):
            res.append(intervals[i])
            i+= 1
            
        
        
        return res
                
        