# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
# 1st Approach (by storing all values of linked list in array, then convert that array into decimal)

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        # Step 1: Stores binary digits from linked list(bin_arr -> binary array)
        bin_arr = []
        node = head
        
        while node:
            # Append binary digit to bin_arr
            bin_arr.append(node.val)  
            node = node.next
        
        # Step 2: Convert binary array to decimal
        decimal = 0
        
        # Start from most significant bit position
        power = len(bin_arr) - 1  
        
        for bit in bin_arr:         
            # Update decimal value based on binary digit
            decimal += bit * (2**power)  
            # Move to next lower bit position
            power -= 1  
        
        return decimal
"""  
# 2nd Approach (Without using additional array)
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        decimal_value = 0
        node = head

        # Traverse the linked list
        while node:
            # Update the decimal value based on the binary digit
            decimal_value = decimal_value * 2 + node.val
            node = node.next

        return decimal_value