# Source : https://leetcode.com/problems/sliding-window-maximum/description/

# Algo/DS : Array, Sliding window, Stack

# Complexity: O(n) n = length of string

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res= []
        stack = []
        if not nums: return []
        for i in range(k):
            if not stack: stack.append(i)
            else:
                while stack and nums[stack[-1]] < nums[i]:
                    stack.pop()
                stack.append(i)
                
        res.append(nums[stack[0]])
        
        for i in range(k, len(nums)):
            if stack[0] == i - k: 
                stack.pop(0)
            while stack and nums[stack[-1]] < nums[i]:
                    stack.pop()
            stack.append(i)
            res.append(nums[stack[0]])
        
        return res
                
                    
        