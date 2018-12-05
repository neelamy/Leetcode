# Source : https://leetcode.com/problems/find-peak-element/description/

# Algo/DS : Binary Search

# Complexity : O(log n)

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        low , high = 0 , len(nums)-1        
        if high == 0 : return high
        while low < high:
            mid = (low+high)/2
            
            # always move towards semi peak and you will
            # eventually get peak
            if nums[mid] >  nums[mid + 1]:
                high = mid
            else:  
                low = mid + 1
                
        return low
            