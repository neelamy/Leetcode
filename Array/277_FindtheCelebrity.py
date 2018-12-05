# Source : https://leetcode.com/problems/find-the-celebrity/description/

# Algo/DS : Array

# Complexity : O(n)

# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        candidate = 0
        
        for ppl in range(1,n):
            if knows(candidate, ppl): candidate = ppl

        for ppl in range(n):
            if ppl!=candidate  and (not knows(ppl, candidate) or knows(candidate,ppl)):return -1
            
        return candidate
        