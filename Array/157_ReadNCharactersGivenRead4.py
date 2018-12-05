# Source : https://leetcode.com/problems/read-n-characters-given-read4/description/

# Algo/DS : Array, Stack

# Complexity : O(n)

# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        
        count = 0
        while True:
            buf4 = [""]*4
            char_read = read4(buf4)
            char_added = min(n - count, char_read)
            if char_added == 0: break 
            for _ in range(char_added):   
                buf[count] = buf4.pop(0)
                count += 1
                
        return count
            
        
        
        