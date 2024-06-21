# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Create a dummy node to handle edge cases
        dummy = ListNode(0)
        dummy.next = head 
        node = dummy  

        while node.next:
            
            # Keep track of the previous node
            prev = node  
            # If current node's value is 0
            if node.next.val == 0:
                # Move to the next node
                node = node.next  
            # If there is a next node
            if node.next:  
                # Merge the current node's value with the next node's value
                node.val += node.next.val
                # Remove the next node by linking the current node to the node after next
                node.next = node.next.next
                
        # Remove the trailing zeros by setting the previous node's next to None
        prev.next = None  
        return head  