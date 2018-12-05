
# https://leetcode.com/problems/lru-cache/description/

# Algo/DS : Linked List, dictionary, LRU

# Complexity :O(1) for get and put

class Node():
    def __init__(self, key,value):
        self.key = key
        self.value = value
        self.next = None
        self.previous =  None
            
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.size = 0
        self.d = {}
        self.head =Node(0,0)
        self.tail =Node(0,0)
        self.head.next = self.tail
        self.tail.previous = self.head
        
 
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """   
        if key in self.d:
            node = self.d[key]
            self.touch(node)
            return node.value            
        return -1
            

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.d:
            node = self.d[key]
            node.value = value
            self.touch(node)
        else:
            node = Node(key, value)
            node.previous = self.head
            node.next = self.head.next
            node.next.previous = node
            self.head.next = node
            self.d[key] = node
            if self.size < self.capacity:               
                self.size += 1               
            else:
                
                p = self.tail.previous
                pp = p.previous
                pp.next = self.tail
                self.tail.previous = pp
                del self.d[p.key]
        return None
                
        
    def touch(self, node):
        p = node.previous
        n_next = node.next
        p.next = n_next
        n_next.previous = p
        node.previous = self.head
        node.next = self.head.next
        node.next.previous = node
        self.head.next = node
        s = self.head.next
      
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)