# Source : https://leetcode.com/problems/search-in-rotated-sorted-array/description/

# Algo/DS : Search

# Complexity : O(log n)


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        left, right = 0 , len(nums) - 1
    
        while left <= right:
            # check if element is at middle
            mid = (left + right) / 2
            if nums[mid] == target : return mid
            
            # this means left is sorted
            if nums[left] <= nums[mid]:
                # check if target in left sorted ot not
                if nums[left] <= target <= nums[mid]: right = mid -1
                else: left = mid + 1
            else:
                # this means right is sorted and so check element in right
                if nums[mid] <= target <= nums[right]: left = mid  + 1
                else: right = mid - 1
    
        return -1
    
    
    
   
   

