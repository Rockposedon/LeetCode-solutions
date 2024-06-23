from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        left = 0
        max_deque = deque()  # Deque to store indices of maximum values
        min_deque = deque()  # Deque to store indices of minimum values
        longest = 0  # Variable to keep track of the longest subarray
        
        for right in range(len(nums)):
            # Maintain max_deque such that elements are in decreasing order
            while max_deque and nums[max_deque[-1]] <= nums[right]:
                max_deque.pop()
            # Maintain min_deque such that elements are in increasing order
            while min_deque and nums[min_deque[-1]] >= nums[right]:
                min_deque.pop()
            
            # Add current index to both deques
            max_deque.append(right)
            min_deque.append(right)
            
            # Ensure the current window satisfies the limit condition
            while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                left += 1
                # Remove elements from the deque if they are out of the current window
                if max_deque[0] < left:
                    max_deque.popleft()
                if min_deque[0] < left:
                    min_deque.popleft()
            
            # Update the longest subarray length
            longest = max(longest, right - left + 1)
        
        return longest
