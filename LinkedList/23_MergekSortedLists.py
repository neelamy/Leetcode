# Source : https://leetcode.com/problems/merge-k-sorted-lists/description/

# Algo/DS : Linked List

# Complexity : O(K) to create heap + mlogK to get smallest element



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


### Longer and slower solution
# class Solution(object):
#     def mergeKLists(self, lists):
#         """
#         :type lists: List[ListNode]
#         :rtype: ListNode
#         """
#         start = ListNode(0)
#         current = start    
      
#         while True:
#             smallest = float("Inf")
#             temp = -1
#             for i in range(len(lists)):
#                 if lists[i] and  smallest > lists[i].val:
#                     smallest = lists[i].val
#                     temp = i
#             if temp == -1 : break
#             current.next = lists[temp]
#             current = current.next
#             lists[temp] = lists[temp].next
#         return start.next
            
        
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []

        # create heap for first element of each list
        for lst in lists:
            if lst : heapq.heappush(heap,(lst.val, lst) )       
        head = ListNode(0)
        current = head

        while heap:
            # get the smallest element
            smallest = heapq.heappop(heap)[1]
            current.next = smallest
            current = current.nextheap

            # if smallest has next element then add it to 
            if smallest.next : heapq.heappush(heap,(smallest.next.val, smallest.next) )
        return head.next
