# Source : https://leetcode.com/problems/reverse-words-in-a-string/description/

# Algo/DS : String

# Complexity : O(n)


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split()       
        return " ".join(s[::-1])
        