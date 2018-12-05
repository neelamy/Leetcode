# Source : https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/

# Algo/DS : Array, Seraching, Binary Search

# Complexity : O(log n) worst case - O(n)

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
      
        low, high = 0, len(nums)-1
    
        
        while low <= high:
            mid = (low  + high)/2
            
            if nums[mid] == target : return True
            #If we know for sure left side is sorted or right side is unsorted
            if nums[low] < nums[mid] or nums[mid] > nums[high]:
                if nums[low] <= target<= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            #If we know for sure right side is sorted or left side is unsorted
            elif nums[mid] < nums[high] or nums[low] > nums[mid] :
                if nums[mid] <= target<= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            #If we get here, that means nums[start] == nums[mid] == nums[end], then shifting out
            #any of the two sides won't change the result but can help remove duplicate from
            #consideration, here we just use high-- but low++ works too
            else: high -=1
            
        return  False
