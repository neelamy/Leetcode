# Source : https://leetcode.com/problems/count-and-say/description/

# Algo/DS : Array, Bactracking

# Complexity : O(n)

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        ans = "1"
        for i in range(n - 1):   
            current_index = 0
            temp = ""
            while current_index < len(ans):
                digit = ans[current_index]
                count = 1
                while current_index + 1 < len(ans) and ans[current_index] == ans[ current_index + 1]: 
                    count += 1
                    current_index += 1
                
                temp += str(count) + digit
                current_index += 1              
            ans = temp
        return ans
        