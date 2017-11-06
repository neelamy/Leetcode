# Source : https://leetcode.com/problems/add-digits/description/

# Algo/DS : Numbers

# Complexity : O(1)

class Solution(object):

    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        #https://en.wikipedia.org/wiki/Digital_root#Congruence_formula
        return 1 +((num-1) % 9) if num > 0 else 0