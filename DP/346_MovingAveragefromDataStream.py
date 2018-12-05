
# Source : https://leetcode.com/problems/moving-average-from-data-stream/description/

# Algo/DS : Array

# Complexity : O(1) for def next

class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.sum = 0
        self.stack = []
        self.count = 0
        self.size = size
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.sum += val
        self.stack.append(val)       
        if self.count < self.size:
            self.count += 1          
        else:
            self.sum -= self.stack[0]
            self.stack.pop(0)             
        return self.sum/(self.count*1.0)
    
    
 # Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)