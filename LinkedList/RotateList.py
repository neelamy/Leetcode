# Source : https://leetcode.com/problems/rotate-list/description/
# Given a list, rotate the list to the right by k places, where k is non-negative.

# Algo/DS : Linked list

# Complexity : O(n)



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None: return head
        fast = head 
        l = 0
        
        # find length of likned list
        while fast:
            l += 1
            fast = fast.next
        k = k % l
        
        fast = head
       
        # move fast ahead by k nodes
        for i in range(k):
            if fast is None : break
            fast = fast.next 
   
        if fast == None : return head            
        
        slow = head
        
        while(fast.next):
            fast = fast.next
            slow = slow.next
            
        fast.next = head    
        head = slow.next
        slow.next = None
        
        return head