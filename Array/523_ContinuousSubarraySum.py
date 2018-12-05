
# Source : https://leetcode.com/problems/continuous-subarray-sum/description/

# Algo/DS : Array,sliding window,

# Complexity :  O(n)

class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d= {}
        d[0] = -1       
        current_sum = 0
        for i in range(len(nums)):
            current_sum += nums[i]

            # find mod
            if k : mod = current_sum % k
            else: mod= current_sum

            # if mod is already present then check length of subarray
            if (mod  in d):
                if i - d[mod] > 1: return True   

            # add mod to dict      
            if mod not in d:
                d[mod] = i
            
        return False