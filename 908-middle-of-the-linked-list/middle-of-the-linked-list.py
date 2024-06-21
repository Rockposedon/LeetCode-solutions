# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        
        # Move fast pointer two steps and slow pointer one step at a time
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # When fast pointer reaches the end, slow pointer will be at the middle
        return slow
"""
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize two pointers, both starting at the head of the list
        l1 = head
        l2 = head
        
        # Traverse the list with l1 moving twice as fast as l2
        while l1 is not None:
            l1 = l1.next  # Move l1 one step ahead
            if l1 is None:
                return l2  # If l1 reaches the end, return l2 as the middle node
            l1 = l1.next  # Move l1 another step ahead
            l2 = l2.next  # Move l2 one step ahead
        
        # In case the loop exits (shouldn't normally reach here due to return above)
        return l2
