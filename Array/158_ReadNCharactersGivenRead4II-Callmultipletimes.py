# Source : https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/description/

# Algo/DS : Array, Stack

# Complexity : O(n)

# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def __init__(self):
        self.buf = []
    
    
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        i = 0        
        while True:

            # create temp buffer
            buf4 = ['']*4

            # chars are read and put in buf4 buffer. This call is needed to update buf4
            # with read chars
            char_read = read4(buf4)

            # append it to self.buf so that for next n , remanining chars can be
            # used from self.buf
            self.buf.extend(buf4)

            # check how many chars are needed
            char_needed = min(n - i, len(self.buf))
   
            # if char needed is 0 then break
            if char_needed == 0: break

            # else append required chars to buf. dont use buf.append.
            # buf array is already provided so just update index value.
            for _ in range(char_needed):             
                buf[i] = self.buf.pop(0)
                i = i + 1
        # return i
        return i
   