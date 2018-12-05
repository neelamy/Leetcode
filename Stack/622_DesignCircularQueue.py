# Source : https://leetcode.com/problems/design-circular-queue/description/

# Algo/DS : Circular Queue

# Complexity : O(n)

class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.queue = [0]*k
        self.front = None
        self.end = None
        

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull() : return False
        
        if self.front == None:
            self.front,self.end = 0,0               
        else:
            self.end = (self.end + 1) % len(self.queue)  
        self.queue[self.end] = value
        return True
              

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty() : return False  
        if self.front == self.end: 
            self.front , self.end = None, None
        else:
            self.front = (self.front + 1) % len(self.queue)
        return True
        

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.front == None : return -1
        return self.queue[self.front]
        

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.end == None : return -1
        return self.queue[self.end]
        

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        if self.front == None : return True        
        return False
        

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        if self.front == None : return False 
        if self.front == 0 and self.end == len(self.queue) - 1: return True
        elif self.end + 1 == self.front : return True
        return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()