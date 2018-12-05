# Source : https://leetcode.com/problems/product-of-array-except-self/description/

# Algo/DS : Array

# Complexity : O(n) space = O(1)

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
  
        n = len(nums)       
        result = [1] * n
        for i in range(1, n):
            result[i] = result[i-1] * nums[i-1]           
        k = 1
        for i in range(n-1, -1, -1):
            result[i] *= k
            k *= nums[i]
        return result
            
        