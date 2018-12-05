# Source : https://leetcode.com/problems/longest-valid-parentheses/description/

# Algo/DS : Array, DP, parentheses

# Complexity : O(n)

'''
If s[i] is '(', set longest[i] to 0,because any string end with '(' cannot be a valid one.

Else if s[i] is ')'

     If s[i-1] is '(', longest[i] = longest[i-2] + 2

     Else if s[i-1] is ')' and s[i-longest[i-1]-1] == '(', longest[i] = longest[i-1] + 2 + longest[i-longest[i-1]-2]

For example, input "()(())", at i = 5, longest array is [0,2,0,0,2,0], longest[5] = longest[4] + 2 + longest[1] = 6.
'''

class Solution(object):

    
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        dp = [0] * len(s)
        
        for i in range(len(s)):
            if s[i] == ')':
                if i > 0 and s[i-1] == "(" : dp[i] = dp[i-2] + 2 if i > 1 else 2
                elif i > 0 and s[i-1] == ")":
                        if i - dp[i-1] - 1 >= 0 and s[i - dp[i-1] - 1] == '(':
                            dp[i] =  2 + dp[i-1] + dp[i - dp[i-1] - 2] if i - dp[i-1] - 2>=0 else 2 + dp[i-1]
                            
        
        return max(dp)