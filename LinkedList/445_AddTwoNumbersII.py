# Source :https://leetcode.com/problems/add-two-numbers-ii/description/

# Algo/DS : Linked List

# Complexity : O(n + m)


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
        
        s1, s2 = [], []
        
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
            
        carry = 0        
        head = None
        
        while carry or s1 or s2:
            sum = carry
            sum += s1.pop() if s1 else 0
            sum += s2.pop() if s2 else 0

            # add new node to the head of existing one
            temp = ListNode(sum % 10)
            carry = sum/10
            temp.next = head if head else None
            head = temp

            
        return head
            
        