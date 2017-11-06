
# Source : https://leetcode.com/problems/balanced-binary-tree/description/

# Algo/DS : Binart Tree

# Complexity : O(n log n)


import string
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        column_letter = [chr(x) for x in range(65,65+27)]#dict(zip( range(0, len(string.uppercase )) , string.uppercase))
        #print column_letter
        ans = ""
        while n:
            ans =  column_letter[ (n-1)%26 ]+ans 
            n = (n-1)/26
            
        return ans