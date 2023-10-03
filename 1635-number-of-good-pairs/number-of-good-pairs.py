class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        # pair are -> i,j
        # iterate in nums
        for i in range(len(nums)):
            # again iterating in nums to knoe is there is good pair 
            for j in range(i+1,len(nums)):
                
                # finding good pairs in nums
                if nums[i] == nums[j] :
                    count += 1
        # return the total number of good pair in varialbe count        
        return count
                    
        