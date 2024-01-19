# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # Initialize both pointers at the head of the linked list
        slow = head
        fast = head

        # Use the "tortoise and hare" approach
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # If there is a cycle, the pointers will meet
            if slow == fast:
                return True

        # If the loop exits, there is no cycle
        return False
        