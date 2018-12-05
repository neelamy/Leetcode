# Source : https://leetcode.com/problems/longest-increasing-subsequence/description/

# Algo/DS : LIS, DP

# Complexity : O(nlog n)

# explanation : https://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums: return 0
        res = [nums[0]]
        
        for i in nums[1:]:
            if i < res[0]: res[0] = i
            elif i >res[-1]: res.append(i)
            else:
                loc = self.bs(res, i)
                res[loc] = i
        return len(res)
        
    
    
    def bs(self, arr, val):
        l , r = 0, len(arr) -1        
        while l < r:            
            mid = (l + r)/ 2
            if arr[mid] == val:
                return mid
                r = mid
            else:
                l = mid + 1
        return l
            