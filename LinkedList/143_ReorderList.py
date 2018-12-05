# Source : https://leetcode.com/problems/reorder-list/description/

# Algo/DS : Linked List 

# Complexity : O(n), space = O(1)


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        first, second = self.split(head)
        
        if second != None:
        
            reversed_list =  self.reverse(second, None)

            final =ListNode(0)
            while first  and reversed_list:
                temp = first.next
                final.next = first
                first = temp
                temp = reversed_list.next
                final.next.next = reversed_list
                reversed_list = temp
                final = final.next.next


            if first:
                final.next = first

            if reversed_list:
                final.next = reversed_list

            head = final.next
            
            
        
        
    def reverse(self, node, prev):
        if not node: return 
        next = node.next
        node.next = prev
        if not next: return node
        return self.reverse(next, node)
    
    def split(self, node):
        if not node or not node.next: 
            return node, None
        slow , fast = node, node.next
        while fast.next and fast.next.next :
            slow = slow.next
            fast= fast.next.next  
        
        start = slow.next
        slow.next = None
        return node, start
            
        