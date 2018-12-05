# Source :https://leetcode.com/problems/kth-largest-element-in-an-array/description/

# Algo/DS : Heap

# Complexity : O((n-k) log k + k)

import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #if len(nums) == 0 : return 
        heap = []
        for i in range(k):
            heapq.heappush(heap, nums[i])
            
        for n in nums[k:]:
            if heapq and heap[0] < n:
                heapq.heapreplace(heap, n)
        return heap[0]
