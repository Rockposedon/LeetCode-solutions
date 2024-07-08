# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        left=head
        mid=head.next
        right=mid.next
        idx=2
        idxs=[]
        while right:
            if (mid.val>left.val and mid.val>right.val) or (mid.val<left.val and mid.val<right.val):
                idxs.append(idx)
            left=mid
            mid=right
            right=right.next
            idx+=1
        if len(idxs)<2:
            return [-1,-1]
        min_dis=float('inf')
        max_dis=idxs[-1]-idxs[0]
        for i in range(1,len(idxs)):
            min_dis=min(min_dis,idxs[i]-idxs[i-1])

        return [min_dis,max_dis]     