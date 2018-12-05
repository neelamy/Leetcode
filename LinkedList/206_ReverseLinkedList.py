# Source : https://leetcode.com/problems/reverse-linked-list/description/

# Algo/DS : Linked List 

# Complexity : O(n), space = O(1)


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.reverse(head, None)
        
        
    def reverse(self, node, prev):
        if not node: return 
        next = node.next
        node.next = prev
        if not next: return node
        return self.reverse(next, node)
       