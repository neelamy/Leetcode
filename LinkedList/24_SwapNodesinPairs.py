# Source : https://leetcode.com/problems/swap-nodes-in-pairs/description/

# Algo/DS : Linked List 

# Complexity : O(n), space = O(1)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        head_final =ListNode(0)
        head_final.next = head
        previous =head_final
        while head and head.next:
            nxt = head.next
            nxt_to_next = nxt.next
            nxt.next = head
            head.next = nxt_to_next
            previous.next = nxt
            previous = head
            head = nxt_to_next
                    
        return head_final.next