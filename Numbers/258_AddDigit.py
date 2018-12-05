	# Source : https://leetcode.com/problems/add-digits/description/

# Algo/DS : Numbers

# Complexity : O(1)

# refer : https://leetcode.com/problems/add-digits/discuss/68667/Simple-Java-Solution-No-recursion-loop
'''
10^k % 9 = 1
a*10^k % 9 = a % 9 
Then let's use an example to help explain.

Say a number x = 23456

x = 2* 10000 + 3 * 1000 + 4 * 100 + 5 * 10 + 6

2 * 10000 % 9 = 2 % 9

3 * 1000 % 9 = 3 % 9

4 * 100 % 9 = 4 % 9

5 * 10 % 9 = 5 % 9

Then x % 9 = ( 2+ 3 + 4 + 5 + 6) % 9, note that x = 2* 10000 + 3 * 1000 + 4 * 100 + 5 * 10 + 6

So we have 23456 % 9 = (2 + 3 + 4 + 5 + 6) % 9

'''
class Solution(object):

    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        #https://en.wikipedia.org/wiki/Digital_root#Congruence_formula
        return 1 +((num-1) % 9) if num > 0 else 0