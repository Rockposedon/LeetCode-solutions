class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        n = len(nums)
        mod = 10**9 + 7
        
        # Adjust the values in nums based on the string s
        for i in range(n):
            if s[i] == "R":
                nums[i] += d
            else:
                nums[i] -= d

        # Initialize variables
        answer = 0
        nums.sort()
        prefix = nums[0]

        # Calculate the sum of distances
        for i in range(1, n):
            left = i * nums[i]
            answer += left - prefix
            prefix += nums[i]

        # Return the answer modulo mod
        return answer % mod
