class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        heapify(nums)
        k_mod = (pow(10, 9) + 7)
        for i in range(k) :
            num = heappop(nums)
            heappush(nums, num+1)

        output = 1
        while nums :
            output *= heappop(nums)
            output %= k_mod

        return output