# Source : https://leetcode.com/problems/copy-list-with-random-pointer/description/

# Algo/DS : Lined List

# Complexity : O(n)


# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """      
        final_head= RandomListNode(0)
        current = final_head
        d = {}
        
        while head:
            new_node = RandomListNode(head.label)
            new_node.random = head
            current.next = new_node
            current = current.next
            d[head] = current           
            head = head.next
            
        current = final_head.next
        while current:
            current.random = d[current.random.random] if current.random.random is not None else None
            current = current.next
            
        return final_head.next
            