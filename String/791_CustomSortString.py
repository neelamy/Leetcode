# Source : https://leetcode.com/problems/custom-sort-string/description/

# Algo/DS : Sort, string, custom sort

# Complexity :O(n + m) 

from collections import Counter
class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        
        # get the char count of T   
        char_count_T = Counter(T)
        
        temp = ""

        # start from 1st char of S
        for char in S:

            # add char in temp 
            temp += char * char_count_T[char]

            # delete char entry from char_count_T
            del char_count_T[char]
         
        # these chars are not in T so add them separately.       
        for char in char_count_T:
            temp += char * char_count_T[char]
        
        # return temp   
        return temp

        