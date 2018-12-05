# Source : https://leetcode.com/problems/basic-calculator/description/

# Algo/DS : string, calculator, stack

# Complexity : O(n)

# read: https://leetcode.com/problems/basic-calculator-iii/discuss/113592/Development-of-a-generic-solution-for-the-series-of-the-calculator-problems



class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        i = 0
        l1,o1= 0,1
        stack = []
        while i < len(s):
           # print i, l1, o1, s[i]
            if s[i].isdigit():
                num = int(s[i])
                while i + 1< len(s) and s[i+1].isdigit():
                    num = num*10 + int(s[i+1])
                    i += 1                    
                l1 = l1 + num if o1 == 1 else l1 - num
            elif s[i] == '(':
                stack .append([l1,o1])
                l1,o1= 0,1
            elif s[i] == ')':
                num = l1
                l1,o1 = stack.pop()
                l1 = l1 + num if o1 == 1 else l1 - num
            elif s[i] in ['+', '-']:
                o1 = 1 if s[i] == '+' else -1
            
            i += 1
                
        return l1
        