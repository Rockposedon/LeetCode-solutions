# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nums = []

        # Traverse the linked list and store the values of nodes in the list
        while head:
            nums.append(str(head.val))  # Convert the value to string and append to the list
            head = head.next  # Move to the next node

        # Concatenate all the values in the list to form a single string
        final_str = "".join(nums)

        # Check if the string formed is equal to its reverse
        if final_str == final_str[::-1]:
            return True  # If equal, return True indicating that the linked list is a palindrome
            
        return False  # If not equal, return False indicating that the linked list is not a palindrome

