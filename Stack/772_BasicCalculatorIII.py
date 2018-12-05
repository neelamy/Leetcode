# Source : https://leetcode.com/problems/basic-calculator-iii/description/

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
        l2,o2 = 1, 1
        stack = []
        while i < len(s):
            #print l1, l2, i, s[i]
            if s[i].isdigit():
                num = int(s[i])
                #i += 1
                while i + 1< len(s) and s[i+1].isdigit():
                    num = num*10 + int(s[i+1])
                    i += 1
                    
                l2 = l2 * num if o2 == 1 else l2 / num
            elif s[i] == '(':
                stack .append([l1,o1, l2, o2])
                l1,o1= 0,1
                l2,o2 = 1, 1
            elif s[i] == ')':
                num = l1 + o1 * l2
                l1,o1, l2, o2 = stack.pop()
                l2 = l2 * num if o2 == 1 else l2 / num
            elif s[i] in ['*', '/']:
                o2 = 1 if s[i] == '*' else -1
            elif s[i] in ['+', '-']:
                l1 = l1 + o1*l2
                l2,o2 = 1, 1
                
                o1 = 1 if s[i] == '+' else -1
            
            i += 1
                
        return l1 + o1*l2
                