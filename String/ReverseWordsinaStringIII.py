# Source : https://leetcode.com/problems/reverse-words-in-a-string-iii/description/
# Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace #and initial word order.

# Algo/DS : String

# Complexity : O(n)

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """        
        return " ".join(map(lambda x :x[::-1], s.split()))
        