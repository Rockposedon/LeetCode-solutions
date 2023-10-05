class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq={}
        ans=[]
        for i in range(0,len(nums)):
            if(nums[i] in freq):
                freq[nums[i]]+=1
            else:
                freq[nums[i]]=0
        for i in freq:
            if freq[i]>=len(nums)//3:
                ans.append(i)
        return ans