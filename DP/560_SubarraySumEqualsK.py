
# Source : https://leetcode.com/problems/subarray-sum-equals-k/description/

# Algo/DS : Array,running sum, DP

# Complexity : O(n) 

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """       
        d = {}

        # important to add this
        d[0] = 1
        running_sum = 0
        result = 0
        for n in nums:
            running_sum += n
            if running_sum - k in d : result += d[running_sum - k]
            d[running_sum] = d.get(running_sum, 0) + 1
            
            
        return result