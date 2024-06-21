# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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