class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxx = max(nums)
        n = len(nums)
        result = 0
        count = 0
        l = 0
        
        for i in range(n):
            if nums[i] == maxx:
                count += 1
            while count >= k:
                if nums[l] == maxx:
                    count -= 1
                l += 1
            result += l
        return result
