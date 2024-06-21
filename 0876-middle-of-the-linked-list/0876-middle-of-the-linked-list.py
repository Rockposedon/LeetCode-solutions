# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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
