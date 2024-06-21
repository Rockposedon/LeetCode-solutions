# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        
        # Pointer to traverse the linked list
        node = head
        
        # Convert the nums list to a set for O(1) lookup times
        num_set = set(nums)
        
        # Initialize the count of connected components to zero
        count = 0
        
        while node:
            # Check if the current node's value is in the set and
            # if it is the end of a component (next node is None or next node's value not in the set)
            if node.val in num_set and (node.next is None or node.next.val not in num_set):
                count += 1  # Increment the component count
                
            # Move to the next node in the linked list
            node = node.next
            
        return count  # Return the total number of connected components
