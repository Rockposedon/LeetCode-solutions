# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

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