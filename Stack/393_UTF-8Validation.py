# Source : https://leetcode.com/problems/utf-8-validation/description/

# Algo/DS : Stack

# Complexity : O(1), space = O(n)


class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """

        # check next val element if they starts with "10"
        def check(val):
            if val > len(binary): return False
            for i in range(val):
                byte = binary.pop(0)
                if not byte.startswith("10"): return False
                
            return True
                
                
                
        # change each int to binary and pad if length < 8        
        binary = []
        for i in data:
            bin_value = bin(i)[2:]
            bin_value = "0" * (8 - len(bin_value)) + bin_value 
            binary.append(bin_value)
        
        # continue till stack
        while binary:

            current = binary.pop(0)

            # skip if its 1 byte
            if current.startswith("0"):                
                continue

            # if its 2 byte then check next 1 element
            if current.startswith("110"): 
                if not check(1): return False
                
            # if its 3 byte then check next 2 element    
            elif current.startswith("1110"):
                if not check(2): return False
            
            # if its 4 byte then check next 3 element   
            elif current.startswith("11110"):
                if not check(3): return False
            else:
                return False
        # return True
        return True
            