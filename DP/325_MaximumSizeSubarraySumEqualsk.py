
# Source : https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/description/

# Algo/DS : Array,running sum, DP

# Complexity : O(n) 

class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        d = {}
        d[0] = -1
        max_len = 0
        running_sum = 0
        for index, n in enumerate(nums):
            running_sum += n
            if running_sum - k in d:
                max_len = max(max_len, index - d[running_sum - k] )
            if running_sum not in d:
                d[running_sum]= index
        return max_len
        