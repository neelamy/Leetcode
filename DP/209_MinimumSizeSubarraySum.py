# Source : https://leetcode.com/problems/minimum-size-subarray-sum/description/

# Algo/DS : Array, DP, sliding window

# Complexity : O(n) n = no of digits

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        
        start, end =0, 0
        
        min_length = float("Inf")
        
        current_sum = 0
        
        while end < len(nums):
            current_sum += nums[end]
            
            while current_sum >= s and start <= end:
                min_length = min(min_length, end - start + 1)
                current_sum -= nums[start]              
                start += 1
            end += 1
            
        return  min_length if min_length != float("Inf") else 0    
                
