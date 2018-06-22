# Source : https://leetcode.com/problems/powx-n/description/

# Algo/DS : Number

# Complexity : O(log n)

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
  
        if n == 0 : return 1 
        if n == 1 : return x
        if  n < 0 : return self.myPow(1/x, -n)
        
        if n%2 == 0:
            return  self.myPow(x * x , n/2)
        else:
            return x * self.myPow(x * x, n/2)
        