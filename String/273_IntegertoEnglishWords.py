# Source : https://leetcode.com/problems/integer-to-english-words/description/

# Algo/DS : string

# Complexity : O(1)

class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        def helper( nums):
            if nums == 0: return ""
            if nums < 20 : return Less_than_20[nums]+ " "
            if nums < 100:
                return Tens[nums/10] + " " + helper(nums%10) 
            else:
                return Less_than_20[nums/100] + " Hundred " + helper(nums%100) 
            
            
        if num == 0 : return  "Zero"
        Less_than_20 =["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        Tens =["","", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"] 
   
        Thousands = ["", "Thousand","Million", "Billion"]
        
        i = 0
        words = ""
        while num > 0:
            if (num % 1000) != 0:
                words = helper(num % 1000) + Thousands[i] + " " + words
            num /= 1000
            i += 1
                
        return words.strip()
    
       