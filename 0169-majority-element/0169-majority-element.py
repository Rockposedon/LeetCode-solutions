# <------------------------------Using Boyer Moore Majority vote algorithm------------------------------------------------>


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        count=0
        result=0
        
        for n in nums:
            if count==0:
                result=n
            if n==result:
                count+=1
            else:
                count-=1
        return result

                
        