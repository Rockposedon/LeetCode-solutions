class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def getCandiesPerChild(mid):
            count = 0
            for candy in candies:
                count += candy // mid
            return count
        
        left, right = 1, sum(candies) // k
        max_candies = 0
        
        while left <= right:
            mid = (left + right) // 2
            if getCandiesPerChild(mid) < k:
                right = mid - 1
            else:
                left = mid + 1
                max_candies = mid
        
        return max_candies
