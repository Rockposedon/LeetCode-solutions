class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        maxlen = 0
        left, right = 0, 0
        counts = defaultdict(int)
        while right < len(nums):
            counts[nums[right]] += 1
            while counts[nums[right]] > k:
                counts[nums[left]] -= 1
                left += 1
            right += 1
            maxlen = max(maxlen, right - left)

        return maxlen