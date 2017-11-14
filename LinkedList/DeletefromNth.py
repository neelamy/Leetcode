# Source : https://leetcode.com/submissions/detail/127169688/

# Algo/DS : Linked list

# Complexity : O(n)


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head is None : return head 
        p1 = head
        p2 = head
        
        for i in range(n):
            p1 = p1.next 
            
        if p1 is None : return head.next
        
            
        while p1.next != None:
            p1 = p1.next
            p2 = p2.next
              
        p2.next = p2.next.next 
        
        return head