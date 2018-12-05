# Source : https://leetcode.com/problems/meeting-rooms-ii/description/

# Algo/DS : Heap, interval

# Complexity : O(nlog k) k = no of room required, n = no of interval


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
import heapq
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        #if len(intervals) == 0 : return 0
        intervals.sort(key = lambda x : x.start)        
        heap = []
        for intv in intervals:

            # heapreplace : removes the smallest element and adds the new one
            if heap and heap[0] <= intv.start:
                heapq.heapreplace(heap, intv.end)
            else:
                heapq.heappush(heap, intv.end)
        return len(heap)
           
        
        