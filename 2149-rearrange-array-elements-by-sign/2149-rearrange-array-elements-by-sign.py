class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos,neg = deque(),deque()

        for num in nums:
            if num>0:
                pos.append(num)
            else:
                neg.append(num)

        for i in range(0,len(nums),2):
            nums[i]=pos.popleft()
            nums[i+1]=neg.popleft()
        return nums