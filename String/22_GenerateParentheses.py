# Source : https://leetcode.com/problems/generate-parentheses/description/

# Algo/DS : String

# Complexity : O(n ^3)

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = ['()']
        if n == 1:
            return ans
        
        
        for i in range(n - 1):
            temp = set()
            for current in ans:
                for pos in range(len(current)):
                    new_list = current[0:pos] + "()" + current[pos:]
                    temp.add(new_list)
            ans = list(temp)
                    
        return ans