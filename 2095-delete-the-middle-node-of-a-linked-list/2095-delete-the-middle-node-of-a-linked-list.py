# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Edge case: If the list is empty or has only one node, return None
        if not head or not head.next:
            return None
        
        # Initialize two pointers and a previous pointer
        slow = head
        fast = head
        prev = None
        
        # Traverse the list with fast moving twice as fast as slow
        while fast and fast.next:
            prev = slow  # Keep track of the node before slow
            slow = slow.next
            fast = fast.next.next
        
        # Delete the middle node
        if prev:
            prev.next = slow.next
        
        # Return the head of the modified list
        return head


        

