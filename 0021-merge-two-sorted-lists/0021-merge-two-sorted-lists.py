# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # if either list is empty return non empty list 
        if not l1:
            return l2
        if not l2:
            return l1
        # check the value of l1 if smaller or equal set l1.next to next node 
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1
        # seet l2.next to next node 
        else:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2
        
