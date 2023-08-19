# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head :
            return
        temp = head
        while head and head.next:
            # Check if the current node's value is the same as the next node's value
            
            if head.val == head.next.val:
                # If a duplicate is found:    
                # Update the next pointer of the current node(remove duplicate)
                head.next = head.next.next
            
            else :
                # If there's no duplicate:
                # Move to the next node in the linked list
                head = head.next
        return temp
            


        
        