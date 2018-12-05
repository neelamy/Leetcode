# Source : https://leetcode.com/problems/largest-number/description/

# Algo/DS : String, sorting

# Complexity : O(n log n) 

class Solution(object):
    
    # we consider a bigger than b if a+b > b+a
    # we want numbers in descending order so change return -1 if a is bigger
    def my_comparator(self, a, b):
        return -1 if a + b > b + a else 1
    
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if sum(nums) == 0 : return "0"
        nums = map(str, nums)
        nums.sort(cmp = self.my_comparator)
        print nums
        
        return "".join(nums)
