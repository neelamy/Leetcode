
# Source : https://leetcode.com/problems/next-greater-element-iii/description/

# Algo/DS : Array, Permutation

# Complexity : O(n**2)

# Explanation : https://leetcode.com/problems/next-permutation/discuss/13867/A-simple-algorithm-from-Wikipedia-with-C++-implementation-(can-be-used-in-Permutations-and-Permutations-II)

class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = map(int,list(str(n)))
        k = -1
        n = len(nums)
        
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                k = i
                break
        if k == -1 : return -1
        l = -1
        for i in range(n-1, k, -1):
            if nums[k] < nums[i]:
                l = i
                break
        nums[k], nums[l]= nums[l], nums[k]
            
        start = k + 1
        last =  n -1
        while start < last:
            nums[start], nums[last] = nums[last], nums[start]
            start +=1
            last -= 1
        nums = map(str, nums)
        nums = int("".join(nums))
        return nums if nums < (2**31) - 1 else -1
        