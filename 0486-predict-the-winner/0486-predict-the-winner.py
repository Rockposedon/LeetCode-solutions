class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def max_score_diff(nums,left,right):
            if left == right :
                return nums[left]
            score_left = nums[left] - max_score_diff(nums,left+1,right)
            score_right = nums[right] - max_score_diff(nums,left,right-1)
            return max(score_left,score_right)
        max_diff = -1
        max_diff = max_score_diff(nums,0,len(nums)-1)
        return max_diff >= 0

