# Source : https://leetcode.com/problems/add-two-numbers/description/

# Algo/DS : Linked list

# Complexity : O(n)


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        c = 0
        start = ListNode(0)
        move = start
        while l1 or l2 or c:
            first = l1.val if l1 else 0
            second = l2.val if l2 else 0
            s = first + second + c
            c = s/10
            node = ListNode(s%10)     
            move.next = node
            move = move.next      
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
                
                
        return start.next