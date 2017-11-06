# Source : https://leetcode.com/problems/two-sum/description/

# Algo/DS : Array

# Complexity : O(n)



class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """       
        d = {}      
        for i, j in enumerate(nums):
            if target - j in d :
                return [d[target - j], i]
            d[j] = i
               
