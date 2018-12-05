# Source : https://leetcode.com/problems/reorganize-string/description/

# Algo/DS : Heap

# Complexity : O(nlog A) A = no of aplhabets, n = length of array

from collections import Counter
from heapq import heappush, heappop
class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        d = Counter(S)

        # get the highest frequency 
        max_freq = d.most_common(1)[0][1]
        
        # if max_freq + (no of spaces required by that char) > len(S): quit
        if max_freq  + (max_freq -1) > len(S) : return ""
        
        # create max heap of chars and their count
        max_heap = []
        for key, val in d.items():
            heappush(max_heap, (-val,key))

        # initialize
        result = ""

        while max_heap:

            # get the top element
            next_char_count,next_char = heappop(max_heap)

            # if its not same as last char in result then add it to result
            # and add it back to heap if freq still more than 1
            if not result or  result[-1] != next_char:
                result = result + next_char
                if next_char_count != -1:
                    heappush(max_heap, (next_char_count + 1,next_char))
            else:

                # else  get the next element, add previous to heap
                # add next char to result and add back to heap if freq> 1
                next_to_next_charcount,next_to_next_char = heappop(max_heap)
                heappush(max_heap, (next_char_count,next_char))
                result = result + next_to_next_char
                if next_to_next_charcount != -1:
                    heappush(max_heap, (next_to_next_charcount + 1,next_to_next_char))
        
        # return result           
        return result
                
  