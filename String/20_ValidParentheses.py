# Source : https://leetcode.com/problems/valid-parentheses/description/

# Algo/DS : String

# Complexity : O(1)

class Solution(object):

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack = []
        
        for i in s:
            if i in["(","[", "{"]: stack.append(i)
            elif len(stack) != 0 and ((i =="}" and stack[-1] =="{") or 
                (i =="]" and stack[-1] =="[") or (i ==")" and stack[-1] =="(") ):
                stack.pop()
            else:
                return False
        return True if len(stack) == 0 else False
        