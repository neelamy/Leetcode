# Source : https://leetcode.com/problems/intersection-of-two-linked-lists/description/

# Algo/DS : Linked List 

# Complexity : O(n), space = O(1)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        l1, l2 = 0,0
        
        startA = headA
        while startA:
            l1+= 1
            startA = startA.next
        
        startB = headB
        while startB:
            l2+= 1
            startB = startB.next
            
        if startB != startA: return None
        
        startA, startB = headA, headB
        while l1> l2:             
            startA = startA.next
            l1 -=1
            
        while l2> l1:
            startB = startB.next
            l2 -=1 
                
        while startA != startB:
            startA = startA.next
            startB = startB.next
            
        return startA
            
                
            
        