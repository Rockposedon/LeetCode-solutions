class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        
        d={0:-1}
        ln=len(nums)
        count=0
        ans=0

        for i in range(ln): 

            if nums[i]==1:
                count+=1
            else:
                count-=1
            
            if count in d:
                ans=max(ans,i-d[count])
            else:
                d[count]=i


        return ans