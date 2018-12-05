# Source : hhttps://leetcode.com/problems/insert-into-a-cyclic-sorted-list/description/

# Algo/DS : Linked List 

# Complexity : O(n), space = O(1)   

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next):
        self.val = val
        self.next = next
"""
class Solution(object):
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        new_node = Node(insertVal, None)
        
        # if not head then return new node
        if not head:
            new_node.next = new_node
            return new_node
        
        current = head
        
        while True:
            
            # if new val lies between current and next then insert
            # 1-->5 val:3
            if current.val <= new_node.val <= current.next.val:
                new_node.next = current.next
                current.next = new_node
                return head

            # this is to check edge case - if val is maximum or minimum
            # eg 5----> 1 val: 0 or 6
            # list is sorted so current < current.next but when current > current.next
            # this means end of sorted list and current is max
            # now check if val is minimum val < current.next or val is max val > currents
            if current.val >= current.next.val and (new_node.val < current.next.val or current.val < new_node.val):
                new_node.next = current.next
                current.next = new_node
                return head
            current = current.next
            
            
            
            
            
        
        