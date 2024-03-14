class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        total_count = 0
        current_sum = 0
        n = len(nums)
        freq = {}
        for i in nums:
            current_sum += i
            if current_sum == goal:
                total_count += 1

            if current_sum - goal in freq:
                total_count += freq[current_sum-goal]
            freq[current_sum] = freq.get(current_sum, 0) + 1
        return total_count