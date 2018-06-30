# Source : https://leetcode.com/problems/rotate-string/description/

# Algo/DS : String

# Complexity : O(n)

class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(B) < len(A) : return False
        A = A+A
        return B in A
