# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        dummy = ListNode(0)
        dummy.next = head
        fast = slow = dummy
        
        # Move the fast pointer n steps ahead
        for _ in range(n):
            fast = fast.next
        
        # Move both pointers until fast reaches the end
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        # Remove the nth node by updating pointers
        slow.next = slow.next.next
        
        return dummy.next
"""
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        totLength = 0
        cur = head

        while cur:
            totLength += 1
            cur = cur.next

        if totLength == n:
            return head.next

        steps = totLength - n - 1
        cur = head
        for _ in range(steps):
            cur = cur.next

        if cur.next:
            cur.next = cur.next.next
        
        return head