class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        seen = []  
        ans = []  
        
        for i in range(n):
            # Check if the leftmost element in 'seen' is out of the current window
            if seen and seen[0] == i - k:
                seen.pop(0)  # Remove the leftmost element if it's out of the window

                
            # Remove elements from 'seen' that are smaller than the current element
            while seen and nums[seen[-1]] < nums[i]:
                seen.pop()  # Keep removing elements until 'seen' is in non-increasing order

                
            seen.append(i)  # Add the current index to 'seen'

            # When the window size is equal to 'k' or greater
            if i >= k - 1:
                ans.append(nums[seen[0]])  # The maximum value in the window is the leftmost element in 'seen'

        return ans  # 'ans' contains the maximum values for each sliding window
