# Source : https://leetcode.com/problems/find-median-from-data-stream/description/

# Algo/DS : Medium, dtream, online

# Complexity : O(n)

import heapq
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_heap =[]
        self.max_heap = []
        self.count = 0
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if (self.count %2) == 0:
            heapq.heappush(self.max_heap, -num)
            if self.min_heap and -self.max_heap[0] >  self.min_heap[0]:
                to_min = - heapq.heappop(self.max_heap)
                to_max = heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, -to_max)
                heapq.heappush(self.min_heap, to_min)
        else:
            heapq.heappush(self.max_heap, -num)
            to_min = - heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, to_min)
        
        self.count += 1
                
            
        

    def findMedian(self):
        """
        :rtype: float
        """
        #print self.max_heap
        if (self.count % 2) != 0:
            return -self.max_heap[0]/1.0
        else:
            return(-self.max_heap[0] + self.min_heap[0]) /2.0
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()