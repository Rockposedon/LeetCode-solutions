# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        if not head:
            return head
        
        node = head
        while node and node.next:
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next
        
        if head.val == val:
            head = head.next
        return head
    


# class Solution:
#     def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
#         # Create a dummy node to simplify edge cases where head needs to be removed
#         dummy = ListNode(0)
#         dummy.next = head
        
#         # Initialize the current pointer to the dummy node
#         current = dummy
        
#         # Traverse the list
#         while current.next:
#             # If the next node has the value to be removed, bypass it
#             if current.next.val == val:
#                 current.next = current.next.next
#             else:
#                 # Otherwise, move to the next node
#                 current = current.next
        
#         # Return the new head, which is the next node of dummy
#         return dummy.next

