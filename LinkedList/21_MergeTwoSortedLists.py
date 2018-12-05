# Source : https://leetcode.com/problems/merge-two-sorted-lists/description/

# Algo/DS : Tree

# Complexity : O(n)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        final_head = ListNode(-1)
        previous = final_head
        while l1 and l2:
            if l1.val <= l2.val: 
                previous.next = l1
                l1 = l1.next
                previous = previous.next
            else:
                previous.next = l2
                l2 = l2.next
                previous = previous.next

        previous.next = l1 or l2

        return final_head.next
                
                    
                
                
                
        