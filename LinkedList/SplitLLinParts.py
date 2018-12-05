# Source : https://leetcode.com/problems/split-linked-list-in-parts/description/
# Given a (singly) linked list with head node root, write a function to split the linked 
#list into k consecutive linked list "parts".

# Algo/DS : Linked list

# Complexity : O(n)

# check this : https://leetcode.com/problems/split-linked-list-in-parts/discuss/109284/Elegant-Python-with-Explanation-45ms
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        
        fast = root 
        
        l = 0
       
        # find length of likned list
        while fast:
            l += 1
            fast = fast.next
            
        s = l / k
        
        remaining = l%k
        
        res = []
        for i in range(k):

            if root is None: 
                res.append([])
                continue
            res.append(root)
            
            move = s + 1 if remaining > 0 else s
            
            remaining -= 1
            
            j = 0
            print " m", move
            while j < move-1 :
                print j ,move, root.val
                root = root.next if root else None
                j += 1

            if root is None : return res
            temp = root.next
            root.next = None if root else None
            root = temp
      
        return res
            
