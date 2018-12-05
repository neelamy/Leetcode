# Source : https://leetcode.com/problems/length-of-last-word/description/

# Algo/DS : String

# Complexity :O(n)


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        return len(s.split()[-1]) if s.strip() else 0
