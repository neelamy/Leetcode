# Source : https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

# Algo/DS : Array

# Complexity : O(log(n))

#refer: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/solution/

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """   
        # find left index   
        left_index = self.binarysearch(nums, target, True)     
        
        # check if left index in range and if target is at left index
        if  left_index == len(nums) or nums[left_index] != target : return [-1,-1]
        
        # find right index. Actual right will be right -1
        right_index = self.binarysearch(nums, target, False)
        
        # return result
        return [left_index, right_index-1]
    
    
    # binary search code
    def binarysearch(self,nums, target, left):
        low, high = 0, len(nums)
        while low < high:
            mid = (low + high)/2

            # if finding left, then move high if mid index has target
            # else for right , move low
            if nums[mid] > target or (left and target == nums[mid]):
                high = mid
            else:
                low = mid + 1
        return low
            