# Source : https://leetcode.com/problems/3sum-smaller/description/

# Algo/DS : Array

# Complexity : O(n^2)


class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        count = 0
        nums = sorted(nums)
        n = len(nums)
        if n < 3: return count 
        i = 0
        while i < n-2:
            if nums[i] <= target/3:
                l = i + 1
                r = n-1

                while l <= r:
                    if nums[i] + nums[l] + nums[r] < target : 
                        count += r - l
                        l  += 1
                    elif nums[i] + nums[l] + nums[r] >= target:
                        r -= 1

                i += 1
        return count