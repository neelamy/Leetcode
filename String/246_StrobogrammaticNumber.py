# Source : https://leetcode.com/problems/strobogrammatic-number/description/

# Algo/DS : String

# Complexity : O(n)

class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        d = {"0": "0","1" :"1", "8": "8","9": "6","6":"9"}
        
        if len(num) ==1 : return num in ["0","1","8"]
        left, right = 0, len(num) -1
        while left<= right:
            if num[left] not in d or num[right] != d[num[left]]: return False
            left += 1
            right -= 1
        return True
            
        