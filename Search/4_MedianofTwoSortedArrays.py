# Source : https://leetcode.com/problems/median-of-two-sorted-arrays/description/

# Algo/DS : Binary Search

# Complexity : O(log min(n1, m1))

# Read: https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/2471/Very-concise-O(log(min(MN)))-iterative-solution-with-detailed-explanation
# or https://www.youtube.com/watch?time_continue=1227&v=LPFhl65R7ww
# https://github.com/mission-peace/interview/blob/master/src/com/interview/binarysearch/MedianOfTwoSortedArrayOfDifferentLength.java

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n1 = len(nums1)
        m1 = len(nums2)
        
        # always make the first array smaller
        if n1 > m1: return self.findMedianSortedArrays(nums2, nums1)
        
        low , high = 0, n1
        
        while low <= high:

            #mid1 is where 1st array is partitioned
            mid1 = (low+high)/2

            # mid2 is where 2nd array is partitioned
            # we have to ensure that total elements on left in both arrays = total elements on right
            # add 1 to handle odd length array
            # this is to ensure that in case of odd length, extra element is on left 
            # if we dont add +1 then extra element will be on right so we will have to use 
            # min(min_x, min_y) if total length is odd
            mid2  = (n1 + m1 + 1)/2 - mid1
            
            # take mid-1 for left and mid for right
            max_x = nums1[mid1-1] if mid1 > 0 else -float("Inf")
            min_x = nums1[mid1] if mid1 < n1 else float("Inf")
            max_y = nums2[mid2-1] if mid2 > 0 else -float("Inf")
            min_y = nums2[mid2] if mid2 < m1 else float("Inf")
            
            if max_x <= min_y and max_y <= min_x:
                if (n1+m1) %2 == 0 :
                    return (max(max_x, max_y) + min(min_x,min_y))/2.0
                else:
                    return max(max_x, max_y)
            elif max_x > min_y:
                high = mid1 - 1
            else:
                low = mid1 + 1
                
        return -1
                
            
        