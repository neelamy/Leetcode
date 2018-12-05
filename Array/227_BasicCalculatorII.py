# Source : https://leetcode.com/problems/basic-calculator-ii/description/

# Algo/DS : Array, String, Stack

# Complexity : O(n) n = length of string

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # to store number
        number = []
        item = ""

        # this will be sign before current number. For 1st number it will be +
        sign = "+"
       
        for i in range(len(s)):

            # store number in item
            if s[i].isdigit():
                item += s[i]
                   
            # if its not number or space or if its end of string(as we need to process last no as well)
            if s[i] in['+', '-', '*', '/'] or i == len(s) - 1:
                item = int(item)
                if sign == "+":number.append(item)
                if sign == "-": number.append(-item)
                if sign == "*": number.append(item * number.pop()) 
                if sign == "/": 
                    if number[-1] > 0 : 
                        number.append(number.pop() / item )       
                    else:
                        # if previous number is -ve then divide without - and put -ve sign later
                        number.append(-(-number.pop() / item))
                
                # reset item
                item = ""

                # set sign to latest opeartor   
                sign = s[i]

       # print number
        return sum(number)