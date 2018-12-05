
# Source : https://leetcode.com/problems/count-primes/description/

# Algo/DS : Number

# Complexity : O(n), Space: O(1)

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n < 2: return 0
        prime = [1]* (n)
        prime[0], prime[1] = 0,0
        for i in range(2,int(n**.5)+ 1):
            if prime[i] == 0: continue
            for j in range(i+i, n, i):
                prime[j] = 0       
        return sum(prime)
                