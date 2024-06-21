# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        # Initialize two pointers, l1 and l2, to the heads of the two linked lists
        l1 = headA
        l2 = headB
        
        # Continue until l1 and l2 point to the same node (i.e., the intersection point)
        while l1!= l2:
            
            # If l1 has reached the end of the first list, start checking from the beginning of the second list
            if l1:
                l1 = l1.next
            else:
                l1 = headB
            
            # If l2 has reached the end of the second list, start checking from the beginning of the first list
            if l2:
                l2 = l2.next
            else:
                l2 = headA
        
        # Return the intersection node (or None if there is no intersection)
        return l1
"""
# 2nd approach using dictionary

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        intersect = {}
        l1 = headA
        l2 = headB
        
        # Traverse the first linked list and store its nodes in the dictionary
        while l1:
            intersect[l1] = True
            l1 = l1.next
        
        # Traverse the second linked list and check if any node is already in the dictionary
        while l2:
            if l2 in intersect:
                return l2
            l2 = l2.next
        
        # If no intersection is found, return None
        return None