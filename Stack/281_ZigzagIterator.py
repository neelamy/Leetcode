# Source :https://leetcode.com/problems/zigzag-iterator/description/

# Algo/DS : stack, deque

# Complexity : O(n)

from collections import deque
class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.array = [v1, v2]
        self.q = deque()

        # for each array, add its first index
        for index, arr in enumerate(self.array):
            if arr:
                self.q.append((index,0))
        

    def next(self):
        """
        :rtype: int
        """
        # get array and its index
        i,j = self.q.popleft()

        # if next index present then add it to queue
        if j+1 < len(self.array[i]): self.q.append((i,j+1))

        # return required item
        return self.array[i][j]
        
        
    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.q)> 0
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())