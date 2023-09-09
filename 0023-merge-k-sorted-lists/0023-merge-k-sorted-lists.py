from heapq import heappush, heappop
from typing import List, Optional

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap, res = [], ListNode()
    
        # Initialize the min-heap with the first node from each list
        for i, lst in enumerate(lists):
            if lst:
                heappush(heap, (lst.val, i, lst))

        cur = res  # 'cur' is a pointer used to build the merged linked list
        while heap:
            _, i, lst = heappop(heap)  # Get the smallest element from the heap
            if lst.next:
                heappush(heap, (lst.next.val, i, lst.next))  # Push the next element of the list to the heap if it exists

            cur.next, cur = lst, lst  # Add the current node to the merged list

        return res.next  # 'res.next' is the merged linked list starting from the first node
